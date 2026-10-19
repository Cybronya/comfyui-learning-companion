---
name: unknown_workflow_sampler_vae_36
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9236
common_nodes: [BasicScheduler, CFGGuider, CreateVideo, DiffusionModelLoaderKJ, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, SaveVideo, TTResolutionSelector, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.5导演台+图生数字人_2087557413565194242.json, 视频生成/图生视频/2063253147182780418.json, 视频生成/文生视频/LTX2.5导演台+文生数字人_2087538824678301697.json, 视频生成/文生视频/LTX2.5导演台_2096907120728956929.json, 视频生成/文生视频/全民导演时代！LTX2.3全流程导演台！_2056554300528218114.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_36

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX2.5导演台+图生数字人_2087557413565194242.json、视频生成/图生视频/2063253147182780418.json、视频生成/文生视频/LTX2.5导演台+文生数字人_2087538824678301697.json、视频生成/文生视频/LTX2.5导演台_2096907120728956929.json、视频生成/文生视频/全民导演时代！LTX2.3全流程导演台！_2056554300528218114.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CreateVideo`
- `DiffusionModelLoaderKJ`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `TTResolutionSelector`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 4/5 个有
- `CLIPLoader` —— 3/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `LTXDirectorGuide` —— 3/5 个有
- `YusuLTXDirector` —— 3/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `DualCLIPLoader` —— 2/5 个有
- `LTXDirector` —— 2/5 个有
- `LTXVCropGuides` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `YusuLTXDirectorCropGuides` —— 2/5 个有
- `YusuLTXDirectorGuide` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `LTXDirectorCropGuides` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
