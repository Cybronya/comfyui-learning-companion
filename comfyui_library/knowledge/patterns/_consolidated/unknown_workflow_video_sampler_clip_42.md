---
name: unknown_workflow_video_sampler_clip_42
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.78325
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, GetNode, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/文生视频+高动态++Remix+Wan2.2 (2)_2054361569718489089.json, 视频生成/图生视频/文生视频+高动态++Smooth+Mix+Wan2.2 (1)_2052573232586346497.json, 视频生成/图生视频/文生视频+高动态+高遵循_2053725147890241538.json, 视频生成/图生视频/最强Wan2.2动漫模型DaSiWa-首尾帧视频_2008457370875207681.json, 视频生成/图生视频/最强Wan2.2模型DaSiWa-首尾帧视频_2009267956248748034.json, 视频生成/图生视频/最强首尾帧视频 - Wan2.2动漫模型DaSiWa-_2009700904043286530.json, 视频生成/图生视频/王中王首尾帧微型--吊打闭源【万物生长 2】_1980857970835804161.json, 视频生成/图生视频/王炸首尾帧--吊打闭源【万物生长 】_1980631743067803649.json, 视频生成/图生视频/王炸首尾帧--吊打闭源【万物生长 】_2013871524415016962.json, 视频生成/图生视频/首尾帧 图生视频 高动态 Wan2.2 Smooth Mix_1978796084820611074.json, 视频生成/图生视频/首尾帧视频-最强Wan2.2动漫模型DaSiWa_2008498194912649217.json, 视频生成/图生视频/首尾帧视频-最强Wan2.2动漫模型DaSiWa_2065475173511417857.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/文生视频+高动态++Remix+Wan2.2 (2)_2054361569718489089.json、视频生成/图生视频/文生视频+高动态++Smooth+Mix+Wan2.2 (1)_2052573232586346497.json、视频生成/图生视频/文生视频+高动态+高遵循_2053725147890241538.json、视频生成/图生视频/最强Wan2.2动漫模型DaSiWa-首尾帧视频_2008457370875207681.json、视频生成/图生视频/最强Wan2.2模型DaSiWa-首尾帧视频_2009267956248748034.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 11/12 个有
- `SeedVR2BlockSwap` —— 11/12 个有
- `SeedVR2ExtraArgs` —— 11/12 个有
- `SeedVR2GGUF` —— 11/12 个有
- `CLIPVisionEncode` —— 9/12 个有
- `CLIPVisionLoader` —— 9/12 个有
- `ImageConcanate` —— 9/12 个有
- `ImageResizeKJ` —— 9/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/12 个有
- `LoadImage` —— 9/12 个有
- `WanFirstLastFrameToVideo` —— 9/12 个有
- `Fast Groups Bypasser (rgthree)` —— 8/12 个有
- `easy textSwitch` —— 5/12 个有
- `ImpactSwitch` —— 4/12 个有
- `CR Text Input Switch (4 way)` —— 3/12 个有
- `Text Concatenate` —— 3/12 个有
- `Wan22PromptSelector` —— 3/12 个有
- `WanImageToVideo` —— 3/12 个有
- `Int` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `PromptTemplateSelector` —— 2/12 个有
- `RH_Nano_Banana_Image2Image` —— 2/12 个有
- `SaveImage` —— 2/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `Images to RGB` —— 1/12 个有
- `Maoyu_ListToString` —— 1/12 个有
- `Qwen3_VQA` —— 1/12 个有
- `YC_SingleTextNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 12 | 100% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler_ancestral | - | 12 | 58% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，12 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，12 个样本，一致性 58%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
