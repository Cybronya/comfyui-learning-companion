# RunningHubRVCOneClickTrain

## 节点类型

`RunningHubRVCOneClickTrain`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:*`（1 次）
- `trainset_dir:STRING`（1 次）
- `experiment_name:STRING`（1 次）
- `save_name:STRING`（1 次）
- `version:COMBO`（1 次）
- `sample_rate:COMBO`（1 次）
- `use_f0:BOOLEAN`（1 次）
- `f0_method:COMBO`（1 次）
- `speaker_id:INT`（1 次）
- `total_epoch:INT`（1 次）

## 输出

- `info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "demo_rvc_train", "demo_rvc_model", "v2", "40k", true, "harvest", 0, 20, 10, 4, 4, true, true, "", "", true, false,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
