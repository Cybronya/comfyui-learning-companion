---
name: unknown_workflow_video_lora_sampler_417
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.940833
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 14B 极速图生视频 优化版_1949991149945708545.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 12步超极速高质量图生视频V1_1949874955704033281.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 6步生视频（无声音）_2056552561905332226.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1954509798727413761.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1993525014328705026.json, 视频生成/图生视频/小狗生成视频_2009159986848473089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_417

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 14B 极速图生视频 优化版_1949991149945708545.json、视频生成/图生视频/Wan2.2 14B+LightX2V 12步超极速高质量图生视频V1_1949874955704033281.json、视频生成/图生视频/Wan2.2 14B+LightX2V 6步生视频（无声音）_2056552561905332226.json、视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1954509798727413761.json、视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1993525014328705026.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `Int` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 12 | 6 | 68% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | lcm | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 12，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
