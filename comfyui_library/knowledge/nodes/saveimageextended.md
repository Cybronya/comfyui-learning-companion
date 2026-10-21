# SaveImageExtended

## 节点类型

`SaveImageExtended`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `positive_text_opt:STRING`（2 次）
- `negative_text_opt:STRING`（2 次）
- `filename_prefix:STRING`（2 次）
- `filename_keys:STRING`（2 次）
- `foldername_prefix:STRING`（2 次）
- `foldername_keys:STRING`（2 次）
- `delimiter:COMBO`（2 次）
- `save_job_data:COMBO`（2 次）
- `job_data_per_image:COMBO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["zit-upscale", "%F %H-%M-%S", "", "QwenEdit", "-", "disabled", false, "", true, 4, "last", true, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
