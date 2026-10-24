---
name: unknown_workflow_sampler_clip_unet_58
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.893643
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/test-z-image_2005514702337830914.json, 图片生成/文生图/Qwen白丝长腿丝袜美腿_2036808073796390913.json, 图片生成/文生图/Qwen黑丝长腿丝袜美腿_2019644098361171969.json, 图片生成/文生图/Z-image文生图18×流_2013868687253573633.json, 图片生成/文生图/Z-image瑜伽舞蹈动作控制_2025505912990994434.json, 图片生成/文生图/Z-image鬼术妖臀蜜桃臀_2027414828809199617.json, 图片生成/文生图/ZImage+LoRA文生图_2018160063252271106.json, 图片生成/文生图/danotebook-qwen-image-2512_2062470910413725697.json, 图片生成/文生图/image_ovis_文生图_1998947182181015554.json, 图片生成/文生图/image_qwen_image2512_2006758711385133057.json, 图片生成/文生图/image_qwen_image2512_grid_scene_2006770240398565377.json, 图片生成/文生图/qwen_image_illustration_lora+全节点注释_2055860239618068481.json, 图片生成/文生图/sugar_coated_gummy_style_qwen+全节点注释_2055855674726338562.json, 图片生成/文生图/黑兽ZImage+LoRA文生图（推荐）_2026928720652541954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/test-z-image_2005514702337830914.json、图片生成/文生图/Qwen白丝长腿丝袜美腿_2036808073796390913.json、图片生成/文生图/Qwen黑丝长腿丝袜美腿_2019644098361171969.json、图片生成/文生图/Z-image文生图18×流_2013868687253573633.json、图片生成/文生图/Z-image瑜伽舞蹈动作控制_2025505912990994434.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/14 个有
- `ModelSamplingAuraFlow` —— 11/14 个有
- `DuckHideNode` —— 4/14 个有
- `LoadImage` —— 3/14 个有
- `INTConstant` —— 2/14 个有
- `Qwen3VL_Chat` —— 1/14 个有
- `SDXLAspectRatio` —— 1/14 个有
- `ShowAnything|Mie` —— 1/14 个有
- `StringConcatenate` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 45 | 14 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 14 | 20% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 45，14 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，14 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（10/14 个样本）：Steps较低可能导致细节不足
