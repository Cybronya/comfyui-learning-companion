# RHUploadMidi

## 节点类型

`RHUploadMidi`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `upload:STRING`（2 次）
- `upload_status:STRING`（2 次）

## 输出

- `MIDI File:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["7ab59c49f90a1d4db1cee44a2463f1a1363d92f14f7dc01a39efc1a8793dc352", "success", "midi file"]`（1 次）
- `["7ab59c49f90a1d4db1cee44a2463f1a1363d92f14f7dc01a39efc1a8793dc352", "success"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
