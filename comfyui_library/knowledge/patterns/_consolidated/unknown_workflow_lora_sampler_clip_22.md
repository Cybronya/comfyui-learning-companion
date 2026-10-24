---
name: unknown_workflow_lora_sampler_clip_22
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.900846
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/👾怪獸-千问漫画转真人👾_1984107523055779842.json, 图片生成/文生图/Qwen_插画海报创作_1955157274396430337.json, 图片生成/文生图/qwen-image文生图官方工作流_1953019372622311426.json, 图片生成/文生图/（老白lokr版-贞贞124500步）Z-Image-Base文生图V1(还没拟合。。)_2019370836720885761.json, 图片生成/文生图/（老白lokr版-贞贞145000步）Z-Image-Base文生图V1(还模型到底还能拟合吗？)_2019682330843025410.json, 图片生成/文生图/（老白lokr版-贞贞165000步）Z-Image-Base文生图V1(这模型到底还能拟合吗？)_2020080899903197186.json, 图片生成/文生图/（老白lokr版-贞贞8W4）Z-Image-Base文生图V1(还没拟合。。)_2018764663516831745.json, 图片生成/文生图/（贞贞版-10W步-none测试）Z-image-base文生图_2035574223229427714.json, 图片生成/文生图/（贞贞版-12W步-none测试）Z-image-base文生图_2035732448901861377.json, 图片生成/文生图/（贞贞版-13W步-none）Z-image-base文生图_2035964999260180482.json, 图片生成/文生图/（贞贞版-15W步-none-最终版）Z-image-base文生图_2036317335383973890.json, 图片生成/文生图/（贞贞版-9W步-none测试）Z-image-base文生图_2034920751538642945.json, 图片生成/文生图/（贞贞版3W步绝美版）Z-Image-Base文生图V1_2016831860403343362.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/👾怪獸-千问漫画转真人👾_1984107523055779842.json、图片生成/文生图/Qwen_插画海报创作_1955157274396430337.json、图片生成/文生图/qwen-image文生图官方工作流_1953019372622311426.json、图片生成/文生图/（老白lokr版-贞贞124500步）Z-Image-Base文生图V1(还没拟合。。)_2019370836720885761.json、图片生成/文生图/（老白lokr版-贞贞145000步）Z-Image-Base文生图V1(还模型到底还能拟合吗？)_2019682330843025410.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `EmptySD3LatentImage` —— 11/13 个有
- `JWFloat` —— 9/13 个有
- `LayerUtility: PurgeVRAM` —— 7/13 个有
- `PreviewImage` —— 2/13 个有
- `EmptyUnitGenerator_UTK` —— 1/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 8 - 50 | 13 | 52% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 13 | 49% |
| 采样算法 | euler | - | 13 | 69% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 8 - 50，13 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，13 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，13 个样本，一致性 69%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
