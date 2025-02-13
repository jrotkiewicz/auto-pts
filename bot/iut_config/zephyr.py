#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2018, Intel Corporation.
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

# Stable Zephyr IUT config

iut_config = {
    # "default": {  # Default west build without option -- -DCONF_FILE=<file.conf>
    #     "test_cases": [
    #         'MESH'
    #     ],
    # },

    "prj.conf": {},  # Default config file name

    "gatt_long_dev_name.conf": {
        "overlay": {
            'CONFIG_BT_EATT_MAX': '5',
            'CONFIG_BT_CONN_DISABLE_SECURITY': 'y',
            'CONFIG_BT_DEVICE_NAME_MAX': '64',
            'CONFIG_BT_DEVICE_NAME': '\"' + 'T' * 63 + '\"',
        },
        "test_cases": [
            'GATT/SR/GAW/BI-33',
        ]
    },

    "l2cap_no_eatt.conf": {
        "overlay": {
            'CONFIG_BT_EATT': 'n',
        },
        "test_cases": [
            'L2CAP/COS/ECFC/BV-01-C',
            'L2CAP/COS/ECFC/BV-02-C',
            'L2CAP/COS/ECFC/BV-03-C',
            'L2CAP/ECFC/BI-01-C',
            'L2CAP/ECFC/BI-02-C',
            'L2CAP/ECFC/BI-03-C',
            'L2CAP/ECFC/BI-04-C',
            'L2CAP/ECFC/BI-05-C',
            'L2CAP/ECFC/BI-06-C',
            'L2CAP/ECFC/BV-01-C',
            'L2CAP/ECFC/BV-02-C',
            'L2CAP/ECFC/BV-03-C',
            'L2CAP/ECFC/BV-04-C',
            'L2CAP/ECFC/BV-06-C',
            'L2CAP/ECFC/BV-07-C',
            'L2CAP/ECFC/BV-08-C',
            'L2CAP/ECFC/BV-09-C',
            'L2CAP/ECFC/BV-10-C',
            'L2CAP/ECFC/BV-11-C',
            'L2CAP/ECFC/BV-12-C',
            'L2CAP/ECFC/BV-13-C',
            'L2CAP/ECFC/BV-14-C',
            'L2CAP/ECFC/BV-15-C',
            'L2CAP/ECFC/BV-16-C',
            'L2CAP/ECFC/BV-17-C',
            'L2CAP/ECFC/BV-18-C',
            'L2CAP/ECFC/BV-19-C',
            'L2CAP/ECFC/BV-20-C',
            'L2CAP/ECFC/BV-21-C',
            'L2CAP/ECFC/BV-22-C',
            'L2CAP/ECFC/BV-23-C',
            'L2CAP/ECFC/BV-24-C',
            'L2CAP/ECFC/BV-25-C',
            'L2CAP/ECFC/BV-26-C',
            'L2CAP/ECFC/BV-27-C',
        ]
    },

    "enforce_mitm.conf": {
        "overlay": {
            'CONFIG_BT_SMP_ENFORCE_MITM': 'y',
        },
        "test_cases": [
            'SM/PER/PKE/BV-05-C',
            'SM/PER/SCPK/BI-04-C',
            'SM/CEN/OOB/BI-01-C',
            'SM/PER/OOB/BV-04-C',
            'SM/PER/OOB/BI-02-C',
            'GAP/SEC/AUT/BV-11-C',
            'GAP/SEC/AUT/BV-12-C',
            'GAP/SEC/AUT/BV-13-C',
        ]
    },

    "sec_priv_mitm.conf": {
        "overlay": {
            'CONFIG_BT_PRIVACY': 'y',
            'CONFIG_BT_SMP_ENFORCE_MITM': 'y',
        },
        "test_cases": [
            'GAP/SEC/SEM/BV-21-C',
            'GAP/SEC/SEM/BV-22-C',
            'GAP/SEC/SEM/BV-26-C',
        ]
    },

    "sec_m1l4.conf": {
        "overlay": {
            'CONFIG_BT_PRIVACY': 'y',
            'CONFIG_BT_SMP_ENFORCE_MITM': 'y',
            'CONFIG_BT_SMP_SC_ONLY': 'y',
            'CONFIG_BT_SMP_SC_PAIR_ONLY': 'y',
        },
        "test_cases": [
            'GAP/SEC/SEM/BV-23-C',
            'GAP/SEC/SEM/BV-24-C',
            'GAP/SEC/SEM/BV-27-C',
            'GAP/SEC/SEM/BV-28-C',
            'GAP/SEC/SEM/BV-29-C',
            'GAP/SEC/SEM/BI-09-C',
            'GAP/SEC/SEM/BI-10-C',
        ]
    },
    "sc_m1l2.conf": {
        "overlay": {
            'CONFIG_BT_PRIVACY': 'y',
            'CONFIG_BT_SMP_ENFORCE_MITM': 'n',
        },
        "test_cases": [
            'GAP/SEC/SEM/BV-37-C',
            'GAP/SEC/SEM/BV-39-C',
            'GAP/SEC/SEM/BV-41-C',
            'GAP/SEC/SEM/BV-43-C',
        ]
    },

    "sc_m1l3.conf": {
        "overlay": {
            'CONFIG_BT_PRIVACY': 'y',
            'CONFIG_BT_SMP_ENFORCE_MITM': 'y',
        },
        "test_cases": [
            'GAP/SEC/SEM/BV-38-C',
            'GAP/SEC/SEM/BV-40-C',
            'GAP/SEC/SEM/BV-42-C',
            'GAP/SEC/SEM/BV-44-C',
        ]
    },

    "privacy.conf": {
        "overlay": {
            'CONFIG_BT_PRIVACY': 'y',
            'CONFIG_BT_RPA_TIMEOUT': '30',
        },
        "test_cases": [
            'GAP/PRIV/CONN/BV-10-C',
            'GAP/PRIV/CONN/BV-11-C',
            'GAP/CONN/ACEP/BV-03-C',  # As of PTS v7.6.2, not supported
            'GAP/CONN/DCEP/BV-05-C',  # As of PTS v7.6.2, not supported
            'GAP/CONN/GCEP/BV-05-C',  # As of PTS v7.6.2, not supported
            'GAP/CONN/NCON/BV-02-C',
            'GAP/CONN/UCON/BV-06-C',
            'GAP/BROB/BCST/BV-03-C',
            'GAP/BROB/BCST/BV-04-C',
            'GAP/BROB/OBSV/BV-06-C',
            'GAP/DISC/RPA/BV-01-C',
            'SM/CEN/KDU/BV-05-C',
            'SM/CEN/KDU/BV-10-C',
            'SM/CEN/KDU/BV-11-C',
            'SM/PER/KDU/BV-02-C',
            'SM/PER/KDU/BV-08-C',
        ]
    },

    "l2cap_param_update.conf": {
        "overlay": {
            'CONFIG_BT_CTLR_CONN_PARAM_REQ': 'n',
        },
        "test_cases": [
            'GAP/CONN/CPUP/BV-01-C',
            'GAP/CONN/CPUP/BV-02-C',
            'GAP/CONN/CPUP/BV-03-C',
            'L2CAP/LE/CPU/BV-01-C',
        ]
    },

    "gap_auto_update_conn_params.conf": {
        "overlay": {
            'CONFIG_BT_GAP_AUTO_UPDATE_CONN_PARAMS': 'n',
        },
        "test_cases": [
            'L2CAP/LE/CFC/BV-06-C',
            'L2CAP/LE/CFC/BV-18-C',
            'L2CAP/LE/CFC/BV-19-C',
            'L2CAP/LE/CFC/BV-21-C',
        ]
    },

    "gap_writable_device_name.conf": {
        "overlay": {
            'CONFIG_BT_DEVICE_NAME_DYNAMIC': 'y',
            'CONFIG_BT_DEVICE_NAME_GATT_WRITABLE': 'y',
            'CONFIG_BT_CONN_DISABLE_SECURITY': 'y',
        },
        'test_cases': [
            'GAP/GAT/BV-05-C',
        ]
    },
}
