---
name: text_to_image_video_lora_sampler_117
type: Text To Image
frequency: 6
level: strong
coverage: 0.9
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3 多模态导演台 加速版_2087009734493827074.json, 视频生成/图生视频/Minimax H3图生视频｜高清视频一键生成直出_2092041097458569217.json, 视频生成/图生视频/超级加速图生视频｜Minimax_h3角色一致性角色表演工作流_2087207226397253634.json, 视频生成/图生视频/超级加速首尾帧图生视频｜Minimax_h3角色一致性角色表演工作流_2087204875179479041.json, 视频生成/文生视频/3步加速Lora｜MiniMaxH3地表最强阿里版，效果炸裂出片快_2099885685254742017.json, 视频生成/文生视频/H3阿里3步加速Lora 效果炸裂视频生成工具_2099913503615311874.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_117

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 多模态导演台 加速版_2087009734493827074.json、视频生成/图生视频/Minimax H3图生视频｜高清视频一键生成直出_2092041097458569217.json、视频生成/图生视频/超级加速图生视频｜Minimax_h3角色一致性角色表演工作流_2087207226397253634.json、视频生成/图生视频/超级加速首尾帧图生视频｜Minimax_h3角色一致性角色表演工作流_2087204875179479041.json、视频生成/文生视频/3步加速Lora｜MiniMaxH3地表最强阿里版，效果炸裂出片快_2099885685254742017.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
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
- `GetImageSize` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MiniMaxH3ImageToVideo` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `EasyCache` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `CreateVideo` —— 3/6 个有
- `INTConstant` —— 3/6 个有
- `PainterVRAM` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `ComfyMathExpression` —— 2/6 个有
- `DiffusionModelLoaderKJ` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `RTXVideoSuperResolution` —— 2/6 个有
- `SpectrumApplyMiniMaxH3` —— 2/6 个有
- `GetVideoComponents` —— 1/6 个有
- `SFH3MultimodalDirector` —— 1/6 个有
- `SaveImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
