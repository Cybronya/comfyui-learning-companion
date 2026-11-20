---
name: unknown_workflow_lora_sampler_clip_148
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.58075
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, CR Text Replace, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/分镜-全能图片pro_2100420944752893954.json, 图片生成/图生图/多宫格分镜图生成-工作台-电影大片感分镜-全平台适用_2039535317241307137.json, 图片生成/图生图/时尚TVC电影四宫格分镜-全能图片pro_2042805070139498497.json, 视频生成/图生视频/时尚TVC电影多宫格分镜&视频生成工作流 V2.0_2068294767087276033.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_148

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/分镜-全能图片pro_2100420944752893954.json、图片生成/图生图/多宫格分镜图生成-工作台-电影大片感分镜-全平台适用_2039535317241307137.json、图片生成/图生图/时尚TVC电影四宫格分镜-全能图片pro_2042805070139498497.json、视频生成/图生视频/时尚TVC电影多宫格分镜&视频生成工作流 V2.0_2068294767087276033.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `Int` —— 3/4 个有
- `ProcessString` —— 3/4 个有
- `RH_RhartImageNProEdit` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `easy anythingIndexSwitch` —— 3/4 个有
- `easy promptLine` —— 3/4 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/4 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | res_multistep | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
