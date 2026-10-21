---
name: text_to_image_upscale_latent_upscale_lora_4
type: Text To Image
frequency: 11
level: strong
coverage: 0.624273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy anythingIndexSwitch, easy cleanGpuUsed]
members: [视频生成/图生视频/H3参考生视频提示词优化二阶高清处理工具_2100427862649171970.json, 视频生成/图生视频/H3真实电影质感正式版_全能参考Latent放大_2100512015759532034.json, 视频生成/图生视频/MiniMax H3 全能参考｜Latent放大 真实电影质感图生视频_2097584321895948290.json, 视频生成/图生视频/MiniMax H3六图可选图生视频混合模型潜空间高清直出工作流，图生视频方案_2107977180578930690.json, 视频生成/图生视频/MiniMax H3电影质感正式版工作流，真实质感文生视频视频生视频图生视频_2106462021058383874.json, 视频生成/图生视频/MiniMax H3真实电影质感无水印正式版 全能参考Latent放大_2109038386567794689.json, 视频生成/图生视频/参考生视频提示词优化二阶高清｜MiniMax H3动作迁移图生视频_2091319533301747713.json, 视频生成/文生视频/H3电影质感正式版 真实电影摄影级视频生成_2099921435648155650.json, 视频生成/文生视频/电影质感视频｜MiniMax H3正式版，文生图生视频都高级_2099918951735185409.json, 视频生成/视频生视频/MiniMax H3电影质感正式版_文生视频图生视频大片感_2106274377644994562.json, 视频生成/视频生视频/MiniMax H3电影质感正式版工作流_真实质感文生视频视频生视频图生视频_2106462021058383874.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/H3参考生视频提示词优化二阶高清处理工具_2100427862649171970.json、视频生成/图生视频/H3真实电影质感正式版_全能参考Latent放大_2100512015759532034.json、视频生成/图生视频/MiniMax H3 全能参考｜Latent放大 真实电影质感图生视频_2097584321895948290.json、视频生成/图生视频/MiniMax H3六图可选图生视频混合模型潜空间高清直出工作流，图生视频方案_2107977180578930690.json、视频生成/图生视频/MiniMax H3电影质感正式版工作流，真实质感文生视频视频生视频图生视频_2106462021058383874.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 11 个 workflow 都包含：
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
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/11 个有
- `LoadAudio` —— 10/11 个有
- `PathchSageAttentionKJ` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `VHS_LoadVideo` —— 10/11 个有
- `H3SigmaRefiner` —— 9/11 个有
- `孤海注释` —— 9/11 个有
- `DisableNoise` —— 8/11 个有
- `H3LatentUpscaleByJingchen573` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `MiniMaxH3BlockCacheT8` —— 8/11 个有
- `easy cleanGpuUsed` —— 8/11 个有
- `SaveImage` —— 7/11 个有
- `GetNode` —— 6/11 个有
- `SetNode` —— 6/11 个有
- `easy anythingIndexSwitch` —— 6/11 个有
- `Fast Groups Muter (rgthree)` —— 5/11 个有
- `FastGroupsBypassSwitch` —— 5/11 个有
- `MiniMaxH3ImageToVideo` —— 5/11 个有
- `PrimitiveInt` —— 5/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `Any Switch (rgthree)` —— 3/11 个有
- `MiniMaxChunkFeedForward` —— 3/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `MiniMaxLowVRAMAttention` —— 3/11 个有
- `MmuuaiGroupBypass` —— 3/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `CR Text Concatenate` —— 2/11 个有
- `ComfySwitchNode` —— 2/11 个有
- `EmptyImage` —— 2/11 个有
- `ManualSigmas` —— 2/11 个有
- `ModelPreviewOverrideKJ` —— 2/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `SpectrumApplyMiniMaxH3` —— 2/11 个有
- `Label (rgthree)` —— 1/11 个有
- `VHS_VideoCombine` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy anythingIndexSwitch、easy cleanGpuUsed
