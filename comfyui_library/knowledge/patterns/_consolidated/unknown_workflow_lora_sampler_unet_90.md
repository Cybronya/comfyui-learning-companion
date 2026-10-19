---
name: unknown_workflow_lora_sampler_unet_90
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CLIPLoader, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json, 视频生成/文生视频/QwenImage2.1洗图_2102985000311418882.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_90

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/AI角色姿态导演台｜Character Pose Director_2102626865503625217.json、视频生成/文生视频/QwenImage2.1洗图_2102985000311418882.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JWString` —— 1/2 个有
- `JWStringConcat` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `QwenImage21Cache` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `VNCCS_PoseStudio` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
