---
name: unknown_workflow_lora_sampler_clip_17
type: Unknown Workflow
frequency: 21
level: weak
coverage: 0.912
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-image-GGUF 海报设计_2013882015992520706.json, 图片生成/文生图/Qwen_插画海报创作_1955157274396430337.json, 图片生成/文生图/Wan2.1 文生图美学去AI感_1950183203102441473.json, 图片生成/文生图/qwen-image gguf 加速版_1955880153337483265.json, 图片生成/文生图/sim▷Qwen中秋节海报特辑_1972281991481782274.json, 图片生成/文生图/【阡陌】Qwen-Image-2512 + 4步加速lora文生图工作流_2008154394784702466.json, 图片生成/文生图/一键生成可爱的小仙女_2029386005651922945.json, 图片生成/文生图/性感情趣内衣亮亮丝袜_2024871763326275585.json, 图片生成/文生图/性感情趣内衣亮亮丝袜_2110944951742844929.json, 图片生成/文生图/自用测试工作流_2017266041059020802.json, 图片生成/文生图/（老白lokr版-贞贞124500步）Z-Image-Base文生图V1(还没拟合。。)_2019370836720885761.json, 图片生成/文生图/（老白lokr版-贞贞145000步）Z-Image-Base文生图V1(还模型到底还能拟合吗？)_2019682330843025410.json, 图片生成/文生图/（老白lokr版-贞贞165000步）Z-Image-Base文生图V1(这模型到底还能拟合吗？)_2020080899903197186.json, 图片生成/文生图/（老白lokr版-贞贞8W4）Z-Image-Base文生图V1(还没拟合。。)_2018764663516831745.json, 图片生成/文生图/（贞贞版-10W步-none测试）Z-image-base文生图_2035574223229427714.json, 图片生成/文生图/（贞贞版-12W步-none测试）Z-image-base文生图_2035732448901861377.json, 图片生成/文生图/（贞贞版-13W步-none）Z-image-base文生图_2035964999260180482.json, 图片生成/文生图/（贞贞版-15W步-none-最终版）Z-image-base文生图_2036317335383973890.json, 图片生成/文生图/（贞贞版-9W步-none测试）Z-image-base文生图_2034920751538642945.json, 图片生成/文生图/（贞贞版3W步绝美版）Z-Image-Base文生图V1_2016831860403343362.json, 图片生成/文生图/（贞贞版）Z-Image-Base 2w2步_2016755186840113154.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/Qwen-image-GGUF 海报设计_2013882015992520706.json、图片生成/文生图/Qwen_插画海报创作_1955157274396430337.json、图片生成/文生图/Wan2.1 文生图美学去AI感_1950183203102441473.json、图片生成/文生图/qwen-image gguf 加速版_1955880153337483265.json、图片生成/文生图/sim▷Qwen中秋节海报特辑_1972281991481782274.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 20/21 个有
- `UNETLoader` —— 18/21 个有
- `EmptySD3LatentImage` —— 16/21 个有
- `LoadImage` —— 13/21 个有
- `LayerUtility: PurgeVRAM` —— 10/21 个有
- `JWFloat` —— 9/21 个有
- `UnetLoaderGGUF` —— 5/21 个有
- `EmptyHunyuanLatentVideo` —— 4/21 个有
- `CompressImages` —— 3/21 个有
- `EmptyUnitGenerator_UTK` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 50 | 21 | 27% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 4 | 21 | 36% |
| 采样算法 | euler | - | 21 | 67% |
| 调度器 | simple | - | 21 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 50，21 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 4，21 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，21 个样本，一致性 67%
- 调度器 最常用 simple，21 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
