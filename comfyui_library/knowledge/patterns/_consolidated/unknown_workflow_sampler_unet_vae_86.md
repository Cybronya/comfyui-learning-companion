---
name: unknown_workflow_sampler_unet_vae_86
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.584455
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 长视频  音频驱动（数字人）唱歌30s_1分钟 切换_2099343389337673730.json, 视频生成/图生视频/MiniMax H3 音频驱动（数字人）唱歌视频_2084544809620041730.json, 视频生成/图生视频/MiniMax H3全能参考生视频_2084114253300199425.json, 视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）_2087383302742298625.json, 视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）（9参考图3视频）_2087443247135281154.json, 视频生成/图生视频/MiniMax H3全能参考生视频（自定义背景+自定义人物+动作迁移）​_2088807649155567617.json, 视频生成/图生视频/MiniMax H3全能参考生视频，图片、视频。音频参考（动作迁移）_2085606340298366977.json, 视频生成/图生视频/h3自定义背景人物换视频背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2092949782200414209.json, 视频生成/图生视频/h3自定义背景换视频背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2092910196111794178.json, 视频生成/图生视频/自定义背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2091761423037853697.json, 视频生成/文生视频/MiniMax H3全能参考生视频（动作迁移）_2084473001717878785.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_86

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 长视频  音频驱动（数字人）唱歌30s_1分钟 切换_2099343389337673730.json、视频生成/图生视频/MiniMax H3 音频驱动（数字人）唱歌视频_2084544809620041730.json、视频生成/图生视频/MiniMax H3全能参考生视频_2084114253300199425.json、视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）_2087383302742298625.json、视频生成/图生视频/MiniMax H3全能参考生视频（LightX2V加速LORA）（9参考图3视频）_2087443247135281154.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/11 个有
- `LoadAudio` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `CR Prompt Text` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 9/11 个有
- `VHS_LoadVideo` —— 8/11 个有
- `MiniMaxH3SigmaShift` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `TrimAudioDuration` —— 2/11 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/11 个有
- `AudioConcat` —— 1/11 个有
- `EasyCache` —— 1/11 个有
- `ImageBatch` —— 1/11 个有
- `MiniMaxH3AddGuide` —— 1/11 个有
- `SelectImages` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有
- `忽略多组孤海` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
