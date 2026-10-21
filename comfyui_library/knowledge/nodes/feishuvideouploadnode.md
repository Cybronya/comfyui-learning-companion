# FeishuVideoUploadNode

## 节点类型

`FeishuVideoUploadNode`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `飞书配置:FEISHU_CONFIG`（4 次）
- `视频输入:VIDEO`（4 次）
- `图片输入:IMAGE`（4 次）
- `音频输入:AUDIO`（4 次）
- `目标列名:STRING`（4 次）
- `筛选条件:STRING`（4 次）
- `创建新行:BOOLEAN`（4 次）
- `新建行数:INT`（4 次）

## 输出

- `视频:VIDEO`（4 次）
- `图片:IMAGE`（4 次）
- `音频:AUDIO`（4 次）
- `状态信息:STRING`（4 次）
- `使用说明:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["图片", "ID+3", false, 1]`（2 次）
- `["视频", "ID+3", false, 1]`（1 次）
- `["音频", "ID+1", false, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
