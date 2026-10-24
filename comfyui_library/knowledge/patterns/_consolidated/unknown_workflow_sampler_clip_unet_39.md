---
name: unknown_workflow_sampler_clip_unet_39
type: Unknown Workflow
frequency: 18
level: weak
coverage: 0.912778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image_1998633899876057090.json, 图片生成/文生图/Z-Image_turbo工作流_2066470777045741570.json, 图片生成/文生图/Z-Image_turbo文生图-又快又好_2100172337105690626.json, 图片生成/文生图/Z-Image_turbo文生图工作流_1995022387781492737.json, 图片生成/文生图/Z-Image_turbo文生图工作流_2032095488664670209.json, 图片生成/文生图/Z-Image动漫加强，简单实用_2002386827807997953.json, 图片生成/文生图/Z-Image动漫加强，简单实用_2005662325996744706.json, 图片生成/文生图/Z-Image动漫加强，简单实用（人脸多样性增强）_2006603694439141377.json, 图片生成/文生图/Z-image-Turbo 文生图_2046797778214461441.json, 图片生成/文生图/Z-image-turbo-t2i_2073765816608313345.json, 图片生成/文生图/Z-image-文生图工作流_2103815728557281281.json, 图片生成/文生图/comfyui教学第一期-文生图_2008024786936537089.json, 图片生成/文生图/image_qwen_Image_2512 BF16_2073295897374584833.json, 图片生成/文生图/image_qwen_image文生图80 年代香港街景_1960500241579520002.json, 图片生成/文生图/image_qwen_image文生图_1984457132592480258.json, 图片生成/文生图/qwen-image-2512工作流_2067229524982587394.json, 图片生成/文生图/qwen2512文生图_2058014938349785090.json, 图片生成/文生图/z_image_文生图（儿童）_2034571865527685121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Z-Image_1998633899876057090.json、图片生成/文生图/Z-Image_turbo工作流_2066470777045741570.json、图片生成/文生图/Z-Image_turbo文生图-又快又好_2100172337105690626.json、图片生成/文生图/Z-Image_turbo文生图工作流_1995022387781492737.json、图片生成/文生图/Z-Image_turbo文生图工作流_2032095488664670209.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 13/18 个有
- `ConditioningZeroOut` —— 10/18 个有
- `ModelSamplingAuraFlow` —— 10/18 个有
- `PrimitiveStringMultiline` —— 6/18 个有
- `easy promptConcat` —— 5/18 个有
- `easy int` —— 4/18 个有
- `Primitive string multiline [Crystools]` —— 1/18 个有
- `PrimitiveString` —— 1/18 个有
- `ResolutionSelector` —— 1/18 个有
- `easy promptLine` —— 1/18 个有
- `easy showAnything` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 8 - 30 | 18 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 18 | 31% |
| 采样算法 | euler | - | 18 | 72% |
| 调度器 | simple | - | 18 | 89% |
| 重绘幅度 | 1 | 0.9 - 1 | 18 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 8 - 30，18 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，18 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，18 个样本，一致性 72%
- 调度器 最常用 simple，18 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，18 个样本，取值集中（一致性 98%）
- 高发问题（15/18 个样本）：Steps较低可能导致细节不足
