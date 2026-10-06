# MiniMaxH3VDNRuntimeAuditT8Advanced

## 节点类型

`MiniMaxH3VDNRuntimeAuditT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `vdn_root:COMBO`（3 次）
- `stage:COMBO`（3 次）
- `verify_hashes:BOOLEAN`（3 次）
- `allow_structural_base:BOOLEAN`（3 次）

## 输出

- `model:MODEL`（3 次）
- `ready:BOOLEAN`（3 次）
- `report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["OpenVDN/vdn-minimax-h3", "stage_dmd_8nfe", true, true]`（2 次）
- `["OpenVDN/vdn-minimax-h3", "stage_dmd_8nfe", false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
