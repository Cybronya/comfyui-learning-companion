# DownloadAndLoadHy3DPaintModel

## 节点类型

`DownloadAndLoadHy3DPaintModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `compile_args:HY3DCOMPILEARGS`（2 次）
- `model:COMBO`（2 次）

## 输出

- `multiview_pipe:HY3DDIFFUSERSPIPE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["hunyuan3d-paint-v2-0"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
