---
name: unknown_workflow_sampler_clip_unet_66
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.980846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/test-z-image_2005514702337830914.json, 图片生成/文生图/Qwen白丝长腿丝袜美腿_2036808073796390913.json, 图片生成/文生图/Qwen黑丝长腿丝袜美腿_2019644098361171969.json, 图片生成/文生图/Z-imageTurbo-intorealism_真实照_2048029631424499714.json, 图片生成/文生图/Z-image文生图18×流_2013868687253573633.json, 图片生成/文生图/Z-image瑜伽舞蹈动作控制_2025505912990994434.json, 图片生成/文生图/Z-image鬼术妖臀蜜桃臀_2027414828809199617.json, 图片生成/文生图/ZImage+LoRA文生图_2018160063252271106.json, 图片生成/文生图/Z_image_turbo_int8_2079199590628282369.json, 图片生成/文生图/z_image_turbo文生图_2011271534962286593.json, 图片生成/文生图/【阡陌】Z-Image随机多样性增强文生图工作流_2009600567135444994.json, 图片生成/文生图/【阡陌】双截棍Nunchaku Z-Image极速文生图工作流_2011317669181526017.json, 图片生成/文生图/本地专用 Z-Image 文生图_2005279973143445506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/test-z-image_2005514702337830914.json、图片生成/文生图/Qwen白丝长腿丝袜美腿_2036808073796390913.json、图片生成/文生图/Qwen黑丝长腿丝袜美腿_2019644098361171969.json、图片生成/文生图/Z-imageTurbo-intorealism_真实照_2048029631424499714.json、图片生成/文生图/Z-image文生图18×流_2013868687253573633.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/13 个有
- `ModelSamplingAuraFlow` —— 10/13 个有
- `ConditioningZeroOut` —— 5/13 个有
- `DuckHideNode` —— 4/13 个有
- `LoadImage` —— 3/13 个有
- `SDXLAspectRatio` —— 3/13 个有
- `ConditioningNoiseInjection` —— 2/13 个有
- `MuyeSizeSelector` —— 1/13 个有
- `NunchakuZImageDiTLoader` —— 1/13 个有
- `Qwen3VL_Chat` —— 1/13 个有
- `ShowAnything|Mie` —— 1/13 个有
- `easy bookmark` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 5 - 16 | 13 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 13 | 3% |
| 采样算法 | euler | - | 13 | 69% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 5 - 16，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，13 个样本，取值分散，一致性仅 3%
- 采样算法 最常用 euler，13 个样本，一致性 69%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（11/13 个样本）：Steps较低可能导致细节不足
