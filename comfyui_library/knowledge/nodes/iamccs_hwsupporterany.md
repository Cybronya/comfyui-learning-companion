# IAMCCS_HwSupporterAny

## 节点类型

`IAMCCS_HwSupporterAny`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `input:*`（3 次）
- `profile:COMBO`（3 次）
- `apply_reserved_vram:BOOLEAN`（3 次）
- `reserved_vram_mode:COMBO`（3 次）
- `reserved_vram_gb:FLOAT`（3 次）
- `reserved_vram_auto_headroom_gb:FLOAT`（3 次）
- `reserved_vram_auto_max_gb:FLOAT`（3 次）
- `fp16_accumulation:COMBO`（3 次）
- `tf32:COMBO`（3 次）
- `clean_gpu_before:BOOLEAN`（3 次）

## 输出

- `output:*`（3 次）
- `report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", true, "manual", 0, 1, 0, "auto", "auto", true, true, false, "overwrite", "GPU: no CUDA\nRAM: RAM ?\nHW profile:`（1 次）
- `["auto", true, "manual", 0, 1, 0, "auto", "auto", false, true, false, "overwrite", "(not probed)", "run", "copy", true]`（1 次）
- `["auto", true, "manual", 0, 1, 0, "auto", "auto", true, true, false, "overwrite", "(not probed)", "run", "copy", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
