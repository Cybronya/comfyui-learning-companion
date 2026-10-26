---
name: image_to_image_sampler_clip_checkpoint
type: Image To Image
frequency: 18
level: moderate
coverage: 0.987667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/0825图生图基础款_2092218913827414017.json, 图片生成/图生图/ComfyUI-图生图例子_1934882440131321858.json, 图片生成/图生图/ComfyUI官方示例2：图生图工作流详解 _ ComfyUI从入门到精通_1931178252860063745.json, 图片生成/图生图/ZIP批量上传图片，for循环处理多张图片演示实例_2046052987583340546.json, 图片生成/图生图/scc图生图_2024066771988258817.json, 图片生成/图生图/图生图基础款212_1970779587238109186.json, 图片生成/图生图/图生图基础款_1933175454839021570.json, 图片生成/图生图/图生图基础款_1938439572621561857.json, 图片生成/图生图/图生图基础款_2015343883298807809.json, 图片生成/图生图/图生图基础款_2027373994801893378.json, 图片生成/图生图/图生图基础款_2031783675611844609.json, 图片生成/图生图/图生图基础款test_1970170069194055682.json, 图片生成/图生图/图生图工作流_2075388564568891394.json, 图片生成/图生图/空白工作流tt_1970172427328253953.json, 图片生成/图生图/简单图生图_2034160543371628545.json, 图片生成/文生图/图生图基础款_1985415351917813761.json, 数字人/数字人/图生图_2059524974226006017.json, 视频生成/图生视频/Seedance2.0 Fast全能参考视频+图生图_2056379103971991553.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/0825图生图基础款_2092218913827414017.json、图片生成/图生图/ComfyUI-图生图例子_1934882440131321858.json、图片生成/图生图/ComfyUI官方示例2：图生图工作流详解 _ ComfyUI从入门到精通_1931178252860063745.json、图片生成/图生图/ZIP批量上传图片，for循环处理多张图片演示实例_2046052987583340546.json、图片生成/图生图/scc图生图_2024066771988258817.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 12/18 个有
- `TextCombinerTwo` —— 11/18 个有
- `CR Text` —— 1/18 个有
- `GetNode` —— 1/18 个有
- `LoadVideo` —— 1/18 个有
- `RH_RhartVideoSparkvideo20FastMultimodalVideo` —— 1/18 个有
- `RH_ViduImageToVideoQ2Pro` —— 1/18 个有
- `SaveVideo` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 15 - 30 | 18 | 86% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 18 | 94% |
| 采样算法 | euler_ancestral | - | 18 | 67% |
| 调度器 | normal | - | 18 | 83% |
| 重绘幅度 | 0.36 | 0.2 - 0.87 | 18 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 15 - 30，18 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，18 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler_ancestral，18 个样本，一致性 67%
- 调度器 最常用 normal，18 个样本，一致性 83%
- 重绘幅度 中位数 0.36，观测区间 0.2 - 0.87，18 个样本
