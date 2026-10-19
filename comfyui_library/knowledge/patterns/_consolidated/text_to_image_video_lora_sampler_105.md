---
name: text_to_image_video_lora_sampler_105
type: Text To Image
frequency: 7
level: strong
coverage: 0.900286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3 多模态导演台 加速版_2087009734493827074.json, 视频生成/图生视频/Minimax H3图生视频｜高清视频一键生成直出_2092041097458569217.json, 视频生成/图生视频/超级加速图生视频｜Minimax_h3角色一致性角色表演工作流_2087207226397253634.json, 视频生成/图生视频/超级加速首尾帧图生视频｜Minimax_h3角色一致性角色表演工作流_2087204875179479041.json, 视频生成/文生视频/3步加速Lora｜MiniMaxH3地表最强阿里版，效果炸裂出片快_2099885685254742017.json, 视频生成/文生视频/H3阿里3步加速Lora 效果炸裂视频生成工具_2099913503615311874.json, 视频生成/文生视频/文生视频基础流｜Minimax_h3一键生成_2093223576789938178.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_105

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 多模态导演台 加速版_2087009734493827074.json、视频生成/图生视频/Minimax H3图生视频｜高清视频一键生成直出_2092041097458569217.json、视频生成/图生视频/超级加速图生视频｜Minimax_h3角色一致性角色表演工作流_2087207226397253634.json、视频生成/图生视频/超级加速首尾帧图生视频｜Minimax_h3角色一致性角色表演工作流_2087204875179479041.json、视频生成/文生视频/3步加速Lora｜MiniMaxH3地表最强阿里版，效果炸裂出片快_2099885685254742017.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `EasyCache` —— 5/7 个有
- `GetImageSize` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `PainterVRAM` —— 4/7 个有
- `ComfyMathExpression` —— 3/7 个有
- `CreateVideo` —— 3/7 个有
- `INTConstant` —— 3/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `DiffusionModelLoaderKJ` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `RTXVideoSuperResolution` —— 2/7 个有
- `SpectrumApplyMiniMaxH3` —— 2/7 个有
- `GetVideoComponents` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `MiniMaxLowVRAMAttention` —— 1/7 个有
- `SFH3MultimodalDirector` —— 1/7 个有
- `SaveImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
