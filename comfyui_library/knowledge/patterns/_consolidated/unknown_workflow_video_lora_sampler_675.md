---
name: unknown_workflow_video_lora_sampler_675
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.288667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, Fast Groups Bypasser (rgthree), GetNode, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SetNode, ShowText|pysssss, Split String, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanAdvancedI2V, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2052912742801125378.json, 视频生成/文生视频/Wan2.2 Remix I2V v2.1 + SVI2Pro 全自动反推长视频工作流_2075174301304713217.json, 视频生成/文生视频/全自动反推长视频工作流-Wan2.2+Remix+I2V+v2.1+SVI2Pro_2066838380490608641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_675

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2052912742801125378.json、视频生成/文生视频/Wan2.2 Remix I2V v2.1 + SVI2Pro 全自动反推长视频工作流_2075174301304713217.json、视频生成/文生视频/全自动反推长视频工作流-Wan2.2+Remix+I2V+v2.1+SVI2Pro_2066838380490608641.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：29%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SetNode`
- `ShowText|pysssss`
- `Split String`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanAdvancedI2V`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `Qwen3_VQA` —— 2/3 个有
- `SomethingToString` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有
- `TextPreview` —— 1/3 个有
- `TextPreviewNode` —— 1/3 个有
- `VHS_LoadVideoFFmpeg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
