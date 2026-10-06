# MZ_ChatGLM3

## 节点类型

`MZ_ChatGLM3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `chatglm3_model:CHATGLM3MODEL`（9 次）
- `hid_proj:TorchLinear`（9 次）
- `text:STRING`（8 次）

## 输出

- `CONDITIONING:CONDITIONING`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一碗牛肉面,撒上葱花,香菜,摄影作品,"]`（5 次）
- `[""]`（3 次）
- `["畸形,粗糙,模糊,低质量,噪点,多余的手,画不好的脸"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
