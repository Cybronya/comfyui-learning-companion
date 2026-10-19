---
name: unknown_workflow_sampler_unet_vae_15
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.823316
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json, 数字人/数字人/7度工作流改版1_2098964914600763393.json, 数字人/数字人/H3数字人_2092831814367924225.json, 数字人/数字人/MiniMax H3开源 数字人音频驱动&图片跳舞 加速版_2089709883632476162.json, 视频生成/图生视频/H3+音频驱动&图片跳舞！加速版_2099306860540162050.json, 视频生成/图生视频/MiniMax H3 长视频  音频驱动（数字人）唱歌30s_1分钟 切换_2099343389337673730.json, 视频生成/图生视频/MiniMax H3开源 数字人音频驱动&图片跳舞 加速版_2089304839850381314.json, 视频生成/图生视频/MiniMax H3开源 数字人音频驱动&图片跳舞 加速版_2089316746447638530.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2087489674502828034.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2087515631137681409.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2094741369498722306.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2094766113983913985.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2099456748556996609.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2099471044871548930.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2110317481368838145.json, 视频生成/图生视频/MiniMax H3开源 音频驱动&图片跳舞 加速版_2110323066374025217.json, 视频生成/图生视频/MiniMaxH3 音频驱动&图片跳舞！加速版！B站艾橘溪_2087001018646220802.json, 视频生成/图生视频/MiniMaxH3数字人_音频驱动&图片跳舞！效果炸裂！_2087444061333581825.json, 视频生成/图生视频/音频驱动图片跳舞加速版｜MiniMax H3_2090000101321302017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_15

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/全能参考视频_Minimax H3_v2_2107298598168915969.json、数字人/数字人/7度工作流改版1_2098964914600763393.json、数字人/数字人/H3数字人_2092831814367924225.json、数字人/数字人/MiniMax H3开源 数字人音频驱动&图片跳舞 加速版_2089709883632476162.json、视频生成/图生视频/H3+音频驱动&图片跳舞！加速版_2099306860540162050.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 18/19 个有
- `LoraLoaderModelOnly` —— 18/19 个有
- `ResolutionSelector` —— 18/19 个有
- `GetNode` —— 17/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/19 个有
- `SetNode` —— 17/19 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 17/19 个有
- `LayerUtility: PurgeVRAM V2` —— 16/19 个有
- `PathchSageAttentionKJ` —— 16/19 个有
- `PainterVRAM` —— 15/19 个有
- `VRAM_Debug` —— 15/19 个有
- `MiniMaxH3SigmaShift` —— 2/19 个有
- `忽略多组孤海` —— 2/19 个有
- `AudioConcat` —— 1/19 个有
- `DF_Int_to_Float` —— 1/19 个有
- `ImageBatch` —— 1/19 个有
- `Int` —— 1/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/19 个有
- `MiniMaxH3AddGuide` —— 1/19 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 1/19 个有
- `PreviewImage` —— 1/19 个有
- `SelectImages` —— 1/19 个有
- `TrimAudioDuration` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
