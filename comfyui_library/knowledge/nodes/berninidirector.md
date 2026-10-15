# BerniniDirector

## 节点类型

`BerniniDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `vae:WANVAE`（5 次）
- `model_high:WANVIDEOMODEL`（5 次）
- `model_low:WANVIDEOMODEL`（5 次）
- `scheduler_high:WANVIDEOSCHEDULER`（5 次）
- `scheduler_low:WANVIDEOSCHEDULER`（5 次）
- `t5_config:BERNINIT5CONFIG`（5 次）
- `high_noise_extra_args:WANVIDSAMPLEREXTRAARGS`（5 次）
- `low_noise_extra_args:WANVIDSAMPLEREXTRAARGS`（5 次）
- `task_type:COMBO`（5 次）
- `global_prompt:STRING`（5 次）

## 输出

- `images:IMAGE`（5 次）
- `audio:AUDIO`（5 次）
- `frame_count:INT`（5 次）
- `report:STRING`（5 次）
- `source_images:IMAGE`（5 次）
- `fps:FLOAT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["v2v — 视频转视频(Video to Video)", "把视频中的金毛换成熊猫", "bad video", "高噪采样设置", 1, 561894922944280, "randomize", true, true, "低噪采样`（1 次）
- `["rv2v — 参考素材改视频", "把视频中的金毛换成熊猫", "bad video", "高噪采样设置", 1, 1073295505514874, "randomize", true, true, "低噪采样设置", 1, 7051`（1 次）
- `["rv2v — 参考素材改视频", "", "bad video", "高噪采样设置", 1, 184393190383510, "randomize", true, true, "低噪采样设置", 1, 25733295003947, `（1 次）
- `["rv2v — 参考素材改视频", "只把源视频人物身上的服装替换为参考图中服装。仅参考服装的颜色、材质、边缘形状、肩带/腰带结构、覆盖范围和贴合方式。保持源视频人物的脸、五官、发型、肤色、体型、身份、动作、表情、镜头、构图、背景和光照不`（1 次）
- `["rv2v — 参考素材改视频", "将视频中的人物替换改为image0的人物", "bad video", "高噪采样设置", 1, 428729732944603, "randomize", true, true, "低噪采样设置",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
