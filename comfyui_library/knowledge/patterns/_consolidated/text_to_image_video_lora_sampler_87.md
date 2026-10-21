---
name: text_to_image_video_lora_sampler_87
type: Text To Image
frequency: 8
level: strong
coverage: 0.89575
common_nodes: [AnyBooleanSwitch, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/三合一效率王｜海螺H3文图首尾帧视频极速生成_2096540420510666754.json, 图片生成/文生图/极速4分钟10秒视频｜海螺H3文图首尾帧三合一_2091014133742399489.json, 图片生成/文生图/极速6分钟1.5M 10秒视频｜海螺H3文图首尾帧三合一标准模式_2092012939061579778.json, 图片生成/文生图/海螺H3文图首尾帧三合一｜10秒视频极速生成工作流_2096473366650777601.json, 图片生成/文生图/海螺H3极速6分钟生成1.5M10秒视频｜文图首尾帧三合一_2097943009395560450.json, 图片生成/文生图/海螺H3极速6分钟视频工作流｜文图首尾帧3合一生成_2097764538979536898.json, 视频生成/文生视频/全能参考练习模式｜H3文生图生视频一键生成_2093263366285512706.json, 视频生成/文生视频/极速4分钟生成10秒视频｜海螺H3全能参考生视频_2091015558560047105.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_87

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/三合一效率王｜海螺H3文图首尾帧视频极速生成_2096540420510666754.json、图片生成/文生图/极速4分钟10秒视频｜海螺H3文图首尾帧三合一_2091014133742399489.json、图片生成/文生图/极速6分钟1.5M 10秒视频｜海螺H3文图首尾帧三合一标准模式_2092012939061579778.json、图片生成/文生图/海螺H3文图首尾帧三合一｜10秒视频极速生成工作流_2096473366650777601.json、图片生成/文生图/海螺H3极速6分钟生成1.5M10秒视频｜文图首尾帧三合一_2097943009395560450.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `AnyBooleanSwitch`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `GetImageSize` —— 6/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `MiniMaxH3ImageToVideo` —— 6/8 个有
- `MinimaxH3LatentUpscaler3D` —— 6/8 个有
- `MiniMaxChunkFeedForward` —— 5/8 个有
- `MiniMaxLowVRAMAttention` —— 5/8 个有
- `easy imageIndexSwitch` —— 5/8 个有
- `MiniMaxH3ReferenceToVideo` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `CM_BoolBinaryOperation` —— 1/8 个有
- `ImpactConditionalBranch` —— 1/8 个有
- `Switch image [Crystools]` —— 1/8 个有
- `VRAM_Debug` —— 1/8 个有
- `easy float` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
