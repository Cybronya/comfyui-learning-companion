---
name: unknown_workflow_sampler_unet_vae_80
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.829636
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 双图15秒原生有声视频 12G低显存增强版_2085579097249505282.json, 视频生成/图生视频/MiniMax H3 咕嘎FC_2085282461919039490.json, 视频生成/图生视频/MiniMax H3 图生视频 升级版_2085717836827287553.json, 视频生成/图生视频/MiniMax H3 多参考图_视频生成视频_2088037369399300097.json, 视频生成/图生视频/MiniMax H3 多参考生视频（本地版）_2084663749595721729.json, 视频生成/图生视频/MiniMax H3 多图生视频+音频接入_2090182586948734978.json, 视频生成/图生视频/MiniMax H3全模态参考生视频工作流｜多图+多视频+多音频统一控制_2084111328754618369.json, 视频生成/图生视频/MiniMaxH3_参考生视频量化加速版_文本_图像_音频_视频_2100207410085457921.json, 视频生成/图生视频/MiniMaxH3_参考生视频量化加速版_文本_图像_音频_视频_2101876284900073474.json, 视频生成/图生视频/无参考视频-新加速高质开源MiniMax H3 RE2VA开源版_2087442373067501569.json, 视频生成/文生视频/MiniMaxH3全能参考生视频1080P开源版（9图3视频3音频）_2084893038450663426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_80

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 双图15秒原生有声视频 12G低显存增强版_2085579097249505282.json、视频生成/图生视频/MiniMax H3 咕嘎FC_2085282461919039490.json、视频生成/图生视频/MiniMax H3 图生视频 升级版_2085717836827287553.json、视频生成/图生视频/MiniMax H3 多参考图_视频生成视频_2088037369399300097.json、视频生成/图生视频/MiniMax H3 多参考生视频（本地版）_2084663749595721729.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 10/11 个有
- `CreateVideo` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `LoadAudio` —— 8/11 个有
- `VHS_LoadVideo` —— 4/11 个有
- `PreviewImage` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `EmptyImage` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `PreviewAny` —— 2/11 个有
- `RHLLMChatNode` —— 2/11 个有
- `SeedVR2LoadDiTModel` —— 2/11 个有
- `SeedVR2LoadVAEModel` —— 2/11 个有
- `SeedVR2VideoUpscaler` —— 2/11 个有
- `EasyCache` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `PainterVRAM` —— 1/11 个有
- `RTXVideoSuperResolution` —— 1/11 个有
- `VHS_VideoCombine` —— 1/11 个有
- `VHS_VideoInfo` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
