---
name: unknown_workflow_lora_sampler_clip_233
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.779333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), ImpactMinMax, KSampler, LoadImage, LoraLoaderModelOnly, ResizeImagesByLongerEdge, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy imageSize, easy imageSizeByLongerSide, easy int, preview_text, text_mul_Join]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/视角切换(ControlNet集成)_2024082972403568641.json, 平台全量/视角切换 (快捷开关)_Qwen_edit_2511_2010022632380440578.json, 平台全量/视角切换(柯基_3D可视化)_Qwen_edit_2511_2009779085538496513.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_233

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/视角切换(ControlNet集成)_2024082972403568641.json、平台全量/视角切换 (快捷开关)_Qwen_edit_2511_2010022632380440578.json、平台全量/视角切换(柯基_3D可视化)_Qwen_edit_2511_2009779085538496513.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImpactMinMax`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ResizeImagesByLongerEdge`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy imageSizeByLongerSide`
- `easy int`
- `preview_text`
- `text_mul_Join`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `QwenMultiangleCameraNode` —— 2/3 个有
- `ResizeLongestToNode` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `Text` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `SaveImagePlus` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
