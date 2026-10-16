# MiniMaxH3VRAMPolicyT8Advanced

## 节点类型

`MiniMaxH3VRAMPolicyT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `mode:COMBO`（2 次）
- `fixed_total_reserved_gib:FLOAT`（2 次）
- `external_margin_gib:FLOAT`（2 次）
- `maximum_reserved_gib:FLOAT`（2 次）
- `clean_before_load:BOOLEAN`（2 次）
- `require_dynamic_vram:BOOLEAN`（2 次）
- `minimum_current_headroom_mib:FLOAT`（2 次）
- `minimum_commit_headroom_gib:FLOAT`（2 次）
- `block_when_commit_below_gate:BOOLEAN`（2 次）
- `policy_epoch:INT`（2 次）

## 输出

- `vram_policy:H3_T8_VRAM_POLICY`（2 次）
- `current_gate_pass:BOOLEAN`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["report_only", 4, 1, 8, false, true, 512, 16, true, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
