---
name: unknown_workflow_lora_sampler_clip_13
type: Unknown Workflow
frequency: 20
level: weak
coverage: 0.89355
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-image-GGUF 海报设计_2013882015992520706.json, 图片生成/文生图/Qwen_插画海报创作_1955157274396430337.json, 图片生成/文生图/Wan2.1 文生图美学去AI感_1950183203102441473.json, 图片生成/文生图/qwen-image gguf 加速版_1955880153337483265.json, 图片生成/文生图/sim▷Qwen中秋节海报特辑_1972281991481782274.json, 图片生成/文生图/【阡陌】Qwen-Image-2512 + 4步加速lora文生图工作流_2008154394784702466.json, 图片生成/文生图/千问文生图快速中文直出2512_2027699940423639041.json, 图片生成/文生图/千问真实幻想V2文生图_1987923112853442561.json, 图片生成/文生图/战双帕米什_赛琳娜 动漫特化人物固定角色-ZImage_2042282589184073730.json, 图片生成/文生图/文生图（自定义lora版）Z-image-base_2018558734011736066.json, 图片生成/文生图/自用测试工作流_2017266041059020802.json, 图片生成/文生图/（老白lokr版-贞贞124500步）Z-Image-Base文生图V1(还没拟合。。)_2019370836720885761.json, 图片生成/文生图/（老白lokr版-贞贞145000步）Z-Image-Base文生图V1(还模型到底还能拟合吗？)_2019682330843025410.json, 图片生成/文生图/（老白lokr版-贞贞165000步）Z-Image-Base文生图V1(这模型到底还能拟合吗？)_2020080899903197186.json, 图片生成/文生图/（老白lokr版-贞贞8W4）Z-Image-Base文生图V1(还没拟合。。)_2018764663516831745.json, 图片生成/文生图/（贞贞版-10W步-none测试）Z-image-base文生图_2035574223229427714.json, 图片生成/文生图/（贞贞版-12W步-none测试）Z-image-base文生图_2035732448901861377.json, 图片生成/文生图/（贞贞版-13W步-none）Z-image-base文生图_2035964999260180482.json, 图片生成/文生图/（贞贞版-15W步-none-最终版）Z-image-base文生图_2036317335383973890.json, 图片生成/文生图/（贞贞版-9W步-none测试）Z-image-base文生图_2034920751538642945.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Qwen-image-GGUF 海报设计_2013882015992520706.json、图片生成/文生图/Qwen_插画海报创作_1955157274396430337.json、图片生成/文生图/Wan2.1 文生图美学去AI感_1950183203102441473.json、图片生成/文生图/qwen-image gguf 加速版_1955880153337483265.json、图片生成/文生图/sim▷Qwen中秋节海报特辑_1972281991481782274.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 19/20 个有
- `UNETLoader` —— 17/20 个有
- `EmptySD3LatentImage` —— 15/20 个有
- `LoadImage` —— 14/20 个有
- `JWFloat` —— 9/20 个有
- `LayerUtility: PurgeVRAM` —— 8/20 个有
- `UnetLoaderGGUF` —— 5/20 个有
- `EmptyHunyuanLatentVideo` —— 4/20 个有
- `CR Text` —— 3/20 个有
- `CR Text Concatenate` —— 2/20 个有
- `EmptyUnitGenerator_UTK` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 50 | 20 | 24% |
| Prompt 约束强度(CFG) | 1.25 | 1 - 4 | 20 | 35% |
| 采样算法 | euler | - | 20 | 70% |
| 调度器 | simple | - | 20 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 50，20 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1.25，观测区间 1 - 4，20 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，20 个样本，一致性 70%
- 调度器 最常用 simple，20 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
