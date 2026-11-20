---
name: unknown_workflow_video_sampler_clip_228
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8075
common_nodes: [AILab_QwenVL, BasicScheduler, CFGGuider, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EasyCache, HunyuanVideo15ImageToVideo, JWInteger, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Hunyuanvideo 1.5 12 steps 480P极速版图生视频（双蒸馏）-自动提示词_1998555121518829569.json, 视频生成/图生视频/Hunyuanvideo 1.5 12 steps 480P极速版图生视频（双蒸馏）_1997551023264829441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_228

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Hunyuanvideo 1.5 12 steps 480P极速版图生视频（双蒸馏）-自动提示词_1998555121518829569.json、视频生成/图生视频/Hunyuanvideo 1.5 12 steps 480P极速版图生视频（双蒸馏）_1997551023264829441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EasyCache`
- `HunyuanVideo15ImageToVideo`
- `JWInteger`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `BatchTextReplace` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `Float` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
