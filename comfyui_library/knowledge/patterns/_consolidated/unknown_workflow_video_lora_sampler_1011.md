---
name: unknown_workflow_video_lora_sampler_1011
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.656
common_nodes: [BasicGuider, BasicScheduler, GetNode, HAIGC_VideoLoader, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, VAEDecode, VAEEncode, VAEEncodeAudio, VHS_VideoCombine, easy clearCacheAll, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3全能参考V3极简版（人脸增强8步二次采样1080p）_2087773102355869698.json, 视频生成/文生视频/MinimaxH3全能参考V5电影画质去油版1_2089032793069277185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1011

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3全能参考V3极简版（人脸增强8步二次采样1080p）_2087773102355869698.json、视频生成/文生视频/MinimaxH3全能参考V5电影画质去油版1_2089032793069277185.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `GetNode`
- `HAIGC_VideoLoader`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeAudio`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `忽略多组孤海`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
