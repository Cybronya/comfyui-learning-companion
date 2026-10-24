---
name: unknown_workflow_sampler_clip_unet_444
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.92
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeHiDream, CR Hires Fix Process Switch, CR Text, CR Text Concatenate, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LayerUtility: PurgeVRAM, PortraitMaster, PortraitMasterStylePose, QuadrupleCLIPLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/文生图/HiDream-I1-dev-bf16 文生图 肖像大师提示词节点_2056177783197446145.json, 图片生成/文生图/HiDream-I1文生图_1923756504455761922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_444

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/HiDream-I1-dev-bf16 文生图 肖像大师提示词节点_2056177783197446145.json、图片生成/文生图/HiDream-I1文生图_1923756504455761922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeHiDream`
- `CR Hires Fix Process Switch`
- `CR Text`
- `CR Text Concatenate`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `PortraitMaster`
- `PortraitMasterStylePose`
- `QuadrupleCLIPLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy clearCacheAll`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
