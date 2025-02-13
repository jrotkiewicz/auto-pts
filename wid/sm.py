#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2017, Intel Corporation.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#

import logging
import sys
import re
from ptsprojects.stack import get_stack
from pybtp import btp

log = logging.debug


def sm_wid_hdl(wid, description, test_case_name, logs=True):
    if logs:
        log("%s, %r, %r, %s", sm_wid_hdl.__name__, wid, description,
            test_case_name)
    module = sys.modules[__name__]

    try:
        handler = getattr(module, "hdl_wid_%d" % wid)
        return handler(description)
    except AttributeError as e:
        logging.exception(e)


def hdl_wid_100(desc):
    btp.gap_conn()
    return get_stack().gap.wait_for_connection(30)


def hdl_wid_101(desc):
    btp.gap_conn()
    return True


def hdl_wid_102(desc):
    btp.gap_disconn()
    return get_stack().gap.wait_for_disconnection(30)


def hdl_wid_104(desc):
    return btp.var_store_get_passkey(desc)


def hdl_wid_106(desc):
    return btp.var_store_get_wrong_passkey(desc)


def hdl_wid_108(desc):
    btp.gap_pair()
    return True


def hdl_wid_109(desc):
    btp.gap_set_mitm_off()
    btp.gap_pair()
    return True


def hdl_wid_110(desc):
    pts_bd_addr = btp.pts_addr_get()
    pts_bd_addr_type = btp.pts_addr_type_get()
    btp.gattc_signed_write(pts_bd_addr_type, pts_bd_addr, "0001", "01")
    return True


def hdl_wid_111(desc):
    # TODO: Verify if the MAC and signed counter has been received correctly
    return True


def hdl_wid_115(desc):
    stack = get_stack()

    btp.gap_set_conn()
    btp.gap_set_gendiscov()
    btp.gap_adv_ind_on(ad=stack.gap.ad, sd=stack.gap.sd)
    return True


def hdl_wid_116(desc):
    # TODO: Click Yes if the failure of pairing process due to timeout has
    # been notified on the IUT.
    return True


def hdl_wid_141(desc):
    return btp.var_store_get_passkey(desc)


def hdl_wid_145(desc):
    """
    Please configure IUT's OOB data flag with 'No remote OOB data present'

    TODO: This is done by default but we should set it explicitly
    """
    return True


def hdl_wid_146(desc):
    """
    Please configure IUT's OOB flag with 'Remote OOB data present'

    TODO: The flag will be set when we handle wid 149 - set remote oob data
    """
    return True


def hdl_wid_147(desc):
    """
    Please enter 16 bytes IUT's OOB Data (confirmation).
    """
    r, c = btp.gap_oob_sc_get_local_data()
    return c


def hdl_wid_148(desc):
    """
    Please enter 16 bytes IUT's OOB Key (random number).
    """
    r, c = btp.gap_oob_sc_get_local_data()
    return r


def hdl_wid_149(desc):
    """
    Please enter the following OOB confirmation and OOB random to the IUT.
    """
    m = re.findall(r"\[([A-Fa-f0-9]+)]", desc)
    conf, rand = m
    btp.gap_oob_sc_set_remote_data(r=rand, c=conf)
    return True


def hdl_wid_152(desc):
    return True


def hdl_wid_154(desc):
    return True


def hdl_wid_155(desc):
    return True


def hdl_wid_156(desc):
    stack = get_stack()
    return not stack.gap.is_connected()


def hdl_wid_1009(desc):
    return btp.var_store_get_passkey(desc)


def hdl_wid_20001(desc):
    stack = get_stack()
    btp.gap_set_conn()
    btp.gap_adv_ind_on(ad=stack.gap.ad)
    return True


def hdl_wid_20100(desc):
    btp.gap_conn()
    return True


def hdl_wid_20011(desc):
    return btp.var_store_get_passkey(desc)


def hdl_wid_20115(desc):
    btp.gap_disconn()
    return True
