# easy controlnetLoaderADV

## 节点类型

`easy controlnetLoaderADV`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（6 次）
- `image:IMAGE`（6 次）
- `control_net:CONTROL_NET`（6 次）

## 输出

- `pipe:PIPE_LINE`（6 次）
- `positive:CONDITIONING`（6 次）
- `negative:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["CN-anytest_v4-marged.safetensors", 0.55, 0, 1, 1]`（1 次）
- `["control_v11p_sd15_canny_fp16.safetensors", 1, 0, 1, 1]`（1 次）
- `["control_v11p_sd15_inpaint.pth", 1, 0, 1, 1]`（1 次）
- `["control_v11f1p_sd15_depth.pth", 0.5, 0, 1, 1]`（1 次）
- `["control_v11p_sd15_canny.pth", 1, 0, 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
