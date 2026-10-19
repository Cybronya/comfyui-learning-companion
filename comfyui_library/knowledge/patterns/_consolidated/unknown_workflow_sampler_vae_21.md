---
name: unknown_workflow_sampler_vae_21
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.935308
common_nodes: [CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 终极导演控制台：时间轴多帧与音视频同步全能工作流_2059175869138165762.json, 视频生成/文生视频/LTX Director （导演节点）多功能 视频生成工作流_2056619920078753794.json, 视频生成/文生视频/LTX2.3 Director 导演工作台_2057724826655219714.json, 视频生成/文生视频/LTX2.3-Director 导演台-多图漫剧长视频_2062370729332662273.json, 视频生成/文生视频/LTX2.3-Director 导演台-多图短剧漫剧长视频_2063220192473341953.json, 视频生成/文生视频/LTX2.3导演分镜台-分镜图+音频+提示词随意控制_2057449564461948929.json, 视频生成/文生视频/LTX2.3导演分镜台工作流——你就是导演（分镜图+音频+提示词随意控制）_2055279773366145027.json, 视频生成/文生视频/LTX2.3导演台 数字人唱歌 短剧自动切分镜 对口型工作流_2057085762369314818.json, 视频生成/文生视频/LTX2.3导演台V2_2081573363293708290.json, 视频生成/文生视频/LTX2.3导演工作流【运镜&分镜编辑】_2056357876544917505.json, 视频生成/文生视频/LTX导演工作流！唱歌对口型 唱歌数字人多分镜 长视频短剧生成_2056389670984048641.json, 视频生成/文生视频/LTX导演工作流！运镜分镜随心所动！_2055019380056043522.json, 视频生成/文生视频/ltx导演节点_2056305995550388226.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_21

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 终极导演控制台：时间轴多帧与音视频同步全能工作流_2059175869138165762.json、视频生成/文生视频/LTX Director （导演节点）多功能 视频生成工作流_2056619920078753794.json、视频生成/文生视频/LTX2.3 Director 导演工作台_2057724826655219714.json、视频生成/文生视频/LTX2.3-Director 导演台-多图漫剧长视频_2062370729332662273.json、视频生成/文生视频/LTX2.3-Director 导演台-多图短剧漫剧长视频_2063220192473341953.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 12/13 个有
- `CreateVideo` —— 12/13 个有
- `LTX2SamplingPreviewOverride` —— 12/13 个有
- `LTXVLatentUpsampler` —— 12/13 个有
- `LatentUpscaleModelLoader` —— 12/13 个有
- `LoraLoaderModelOnly` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `CheckpointLoaderSimple` —— 7/13 个有
- `VAEDecodeTiled` —— 7/13 个有
- `VAEDecode` —— 6/13 个有
- `UNETLoader` —— 5/13 个有
- `GetNode` —— 2/13 个有
- `ManualSigmas` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `VHS_VideoCombine` —— 2/13 个有
- `DNode_CameraShakeLissajous` —— 1/13 个有
- `ImpactSwitch` —— 1/13 个有
- `LTXVChunkFeedForward` —— 1/13 个有
- `LoadVideo` —— 1/13 个有
- `PreviewAudio` —— 1/13 个有
- `UnetLoaderGGUF` —— 1/13 个有
- `VAELoader` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
