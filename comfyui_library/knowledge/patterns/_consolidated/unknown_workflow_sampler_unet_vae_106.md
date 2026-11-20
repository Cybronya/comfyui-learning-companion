---
name: unknown_workflow_sampler_unet_vae_106
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.856182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3 面部重绘 FACE REFINE 修复崩脸_2090087014422110210.json, 视频生成/图生视频/H3-参考生视频（全能参考）_2087759964113821697.json, 视频生成/图生视频/MiniMax H3  动画与风格化影像_2084557369203322882.json, 视频生成/图生视频/MiniMax H3 -多图参考生视频_2084163028865609729.json, 视频生成/图生视频/MiniMax H3 3参考图生成跳舞视频_2089373518189383681.json, 视频生成/图生视频/MiniMax H3 8步加速 智能参考娃娃穿搭视频生成_2085536956800397314.json, 视频生成/图生视频/MiniMax H3 ComfyUI多图（音视频）参考模板工作流（官方模板）_2085042609009020929.json, 视频生成/图生视频/MiniMax H3 Ref2VA多图参考生视频-导演级官方提示词标准化模板_2084942982297505793.json, 视频生成/图生视频/MiniMax H3 参考生视频_2084543006513909761.json, 视频生成/图生视频/MiniMax H3 参考生视频_2085194930540077058.json, 视频生成/图生视频/MiniMax H3 参考生视频（Sage加速）2608_2085826399662854146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_106

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/H3 面部重绘 FACE REFINE 修复崩脸_2090087014422110210.json、视频生成/图生视频/H3-参考生视频（全能参考）_2087759964113821697.json、视频生成/图生视频/MiniMax H3  动画与风格化影像_2084557369203322882.json、视频生成/图生视频/MiniMax H3 -多图参考生视频_2084163028865609729.json、视频生成/图生视频/MiniMax H3 3参考图生成跳舞视频_2089373518189383681.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `PrimitiveStringMultiline` —— 10/11 个有
- `EasyCache` —— 5/11 个有
- `PathchSageAttentionKJ` —— 5/11 个有
- `VHS_LoadVideo` —— 4/11 个有
- `LoadAudio` —— 3/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/11 个有
- `VHS_VideoCombine` —— 2/11 个有
- `FlashVSRInitPipe` —— 1/11 个有
- `FlashVSRNodeAdv` —— 1/11 个有
- `H3FaceStitch` —— 1/11 个有
- `H3FaceTrackCrop` —— 1/11 个有
- `H3InjectVideoLatent` —— 1/11 个有
- `H3PerFrameDenoise` —— 1/11 个有
- `MiniMaxH3NativeAudioLock` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有
- `忽略多组孤海` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
