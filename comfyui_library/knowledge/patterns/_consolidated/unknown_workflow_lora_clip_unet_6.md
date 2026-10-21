---
name: unknown_workflow_lora_clip_unet_6
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.613667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, Fast Groups Bypasser (rgthree), INTConstant, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, easy seed]
members: [图片生成/文生图/1988189438566162434.json, 图片生成/文生图/wan22文生图-普通采样器版_2016569115120504833.json, 图片生成/文生图/wan22文生图-高级采样器版_2016541489207189506.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1988189438566162434.json、图片生成/文生图/wan22文生图-普通采样器版_2016569115120504833.json、图片生成/文生图/wan22文生图-高级采样器版_2016541489207189506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `DF_Float` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 3 | 33% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 3 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 6，3 个样本，一致性 33%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 最常用 1，3 个样本，一致性 33%
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、easy seed
