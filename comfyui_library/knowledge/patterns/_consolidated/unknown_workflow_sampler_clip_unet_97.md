---
name: unknown_workflow_sampler_clip_unet_97
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.95325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/test-z-image_2005514702337830914.json, 图片生成/文生图/Qwen白丝长腿丝袜美腿_2036808073796390913.json, 图片生成/文生图/Qwen黑丝长腿丝袜美腿_2019644098361171969.json, 图片生成/文生图/Z-imageTurbo-intorealism_真实照_2048029631424499714.json, 图片生成/文生图/Z-image文生图18×流_2013868687253573633.json, 图片生成/文生图/Z-image瑜伽舞蹈动作控制_2025505912990994434.json, 图片生成/文生图/Z-image鬼术妖臀蜜桃臀_2027414828809199617.json, 图片生成/文生图/ZImage+LoRA文生图_2018160063252271106.json, 图片生成/文生图/image_qwen_image2512_2006758711385133057.json, 图片生成/文生图/image_qwen_image2512_grid_scene_2006770240398565377.json, 图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json, 图片生成/文生图/黑兽ZImage+LoRA文生图（推荐）_2026928720652541954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_97

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/test-z-image_2005514702337830914.json、图片生成/文生图/Qwen白丝长腿丝袜美腿_2036808073796390913.json、图片生成/文生图/Qwen黑丝长腿丝袜美腿_2019644098361171969.json、图片生成/文生图/Z-imageTurbo-intorealism_真实照_2048029631424499714.json、图片生成/文生图/Z-image文生图18×流_2013868687253573633.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/12 个有
- `ModelSamplingAuraFlow` —— 9/12 个有
- `DuckHideNode` —— 4/12 个有
- `INTConstant` —— 3/12 个有
- `LoadImage` —— 2/12 个有
- `SDXLAspectRatio` —— 2/12 个有
- `MemoryCleaner` —— 1/12 个有
- `Qwen3VL_Chat` —— 1/12 个有
- `ShowAnything|Mie` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 16 | 12 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 12 | 3% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 16，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，12 个样本，取值分散，一致性仅 3%
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（10/12 个样本）：Steps较低可能导致细节不足
