---
name: unknown_workflow_lora_sampler_clip_161
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8825
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, RH_Captioner, TextBox, UNETLoader, VAEDecode, VAELoader, WanImageToVideo, easy ifElse, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 电影级画面图生视频_1950023437323517954.json, 视频生成/图生视频/Wan2.2-高速版-直出720p -自动提示词_1949982975842803713.json, 视频生成/图生视频/wan2.2_14B_自动提示词优化_图生视频-加速版-KJ模型_1950557926803099649.json, 视频生成/图生视频/图生视频工作流_2013427076698742785.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 电影级画面图生视频_1950023437323517954.json、视频生成/图生视频/Wan2.2-高速版-直出720p -自动提示词_1949982975842803713.json、视频生成/图生视频/wan2.2_14B_自动提示词优化_图生视频-加速版-KJ模型_1950557926803099649.json、视频生成/图生视频/图生视频工作流_2013427076698742785.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RH_Captioner`
- `TextBox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `Primitive integer [Crystools]` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `LoadImagesFromURL` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 7 | 6 - 8 | 4 | 90% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 8，4 个样本，取值集中（一致性 90%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
