---
name: unknown_workflow_sampler_unet_vae_125
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/MINIMAX-H3 参考图像-视频-音频生成视频_2101539650572742657.json, 平台全量/MINIMAX-H3 参考图像-视频-音频生成视频_2101910069695832066.json, 平台全量/MiniMaxH3_参考生视频量化加速版_文本_图像_音频_视频_2100873035296370689.json, 平台全量/MiniMaxH3_参考生视频量化加速版_文本_图像_音频_视频_2101139002450604033.json, 平台全量/Minimax H3视频模型参考生视频_2084172867280916482.json, 平台全量/Minimax h3 高一致性-故事多分镜图处理_2092582271432876034.json, 视频生成/图生视频/AIDir-MinimaxH3全能参考多人物短剧工作流(开源量化加速版)速度提升质量不减_2087041425555939329.json, 视频生成/图生视频/H3 参考图像-视频-音频生成视频_2084427820587114497.json, 视频生成/图生视频/H3 数字人和声音克隆。_2084429432323928065.json, 视频生成/图生视频/h3-参考生成视频-加速版_2085877996057088001.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_125

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/MINIMAX-H3 参考图像-视频-音频生成视频_2101539650572742657.json、平台全量/MINIMAX-H3 参考图像-视频-音频生成视频_2101910069695832066.json、平台全量/MiniMaxH3_参考生视频量化加速版_文本_图像_音频_视频_2100873035296370689.json、平台全量/MiniMaxH3_参考生视频量化加速版_文本_图像_音频_视频_2101139002450604033.json、平台全量/Minimax H3视频模型参考生视频_2084172867280916482.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 8/10 个有
- `VHS_LoadVideo` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `PathchSageAttentionKJ` —— 6/10 个有
- `SaveImage` —— 6/10 个有
- `CreateVideo` —— 5/10 个有
- `FlashVSRNode` —— 5/10 个有
- `LoraLoaderBypassModelOnly` —— 5/10 个有
- `Sleep` —— 5/10 个有
- `PainterVRAM` —— 4/10 个有
- `SaveVideo` —— 3/10 个有
- `EasyCache` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `GetVideoComponents` —— 2/10 个有
- `Audio Duration (mtb)` —— 1/10 个有
- `AudioCrop` —— 1/10 个有
- `GetImagesFromBatchIndexed` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `SaveAudioAdvanced` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
