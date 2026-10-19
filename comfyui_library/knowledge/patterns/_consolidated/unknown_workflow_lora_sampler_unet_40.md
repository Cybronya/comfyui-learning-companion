---
name: unknown_workflow_lora_sampler_unet_40
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95175
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3-二采多图参考（4步加速_官方节点版）_2090604828555825154.json, 视频生成/文生视频/H3 LightX2V 二采高清图_文生视频_2087548123051806721.json, 视频生成/文生视频/Minimax-H3 多图参考_产品介绍视频_2090089362729033729.json, 视频生成/文生视频/Minimax-H3-4步加速-单图参考（二次采样_官方节点版）_2090043814345007105.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_40

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3-二采多图参考（4步加速_官方节点版）_2090604828555825154.json、视频生成/文生视频/H3 LightX2V 二采高清图_文生视频_2087548123051806721.json、视频生成/文生视频/Minimax-H3 多图参考_产品介绍视频_2090089362729033729.json、视频生成/文生视频/Minimax-H3-4步加速-单图参考（二次采样_官方节点版）_2090043814345007105.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 3/4 个有
- `Float` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `RTXVideoSuperResolution` —— 3/4 个有
- `Text` —— 3/4 个有
- `VRAMReserver` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy clearCacheAll` —— 3/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
