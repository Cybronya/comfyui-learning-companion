# RunningHub_MOVA_Sampler

## 节点类型

`RunningHub_MOVA_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `pipeline:RH_MOVA_Pipeline`（7 次）
- `reference_image:IMAGE`（7 次）
- `prompt:STRING`（7 次）
- `width:INT`（7 次）
- `height:INT`（7 次）
- `num_frames:INT`（7 次）
- `fps:FLOAT`（7 次）
- `steps:INT`（7 次）
- `cfg_scale:FLOAT`（7 次）
- `seed:INT`（7 次）

## 输出

- `video:VIDEO`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A person speaks naturally in a casual setting. They say, \"Hello, this is a test of the MOVA video generation system.\`（1 次）
- `["在星空下，一位白发女子站在地上，手持一把闪耀着光芒的长剑。她踏过水面，高举长剑，剑身被金色的光环环绕。她高声呼喊：“凭借此剑，我斩妖除魔！”随后挥剑向前，将远处的建筑一劈为二。", 352, 640, 97, 24, 25, 5, 22`（1 次）
- `["美女在电梯里面自拍，转了个圈，嘴里自信的说着：“真好看！”", 352, 640, 97, 24, 25, 5, 2517505233, "randomize", "", 5, false]`（1 次）
- `["一个女生对着镜头撒娇。她说：“遇到难回答的问题，就不说话了。”", 640, 352, 97, 24, 25, 5, 3100728657, "randomize", "", 5, false]`（1 次）
- `["A person speaks naturally in a casual setting. They say, \"Hello, this is a test of the MOVA video generation system.\`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
