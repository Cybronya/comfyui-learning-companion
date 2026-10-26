---
name: unknown_workflow_upscale_checkpoint
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.802235
common_nodes: [CheckpointLoaderSimple, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, ShowText|pysssss, WujiCleaner, WujiEditor, WujiUpscaler]
problems: []
missing: []
members: [图片生成/反推提示词/85jiaosezichanku_2034622358798999554.json, 图片生成/图生图/AI短剧文生空场景专用+自动扩写专用提示词-邻家AI大女孩_2043344708990144514.json, 图片生成/图生图/AI短剧文生空场景专用Qwen-image+自动扩写专用提示词_1961070208133873665.json, 图片生成/图生图/AI短剧文生空场景专用Qwen-image+自动扩写专用提示词_2039157804702900225.json, 图片生成/文生图/AI短剧文生空场景专用Qwen-image+自动扩写专用提示词_2045052390331654146.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imageZIB模型_2026133088706764802.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imageZIB模型_2048716562764402689.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-imagebaseZIB模型_2026178597890826241.json, 图片生成/文生图/SeeDance 2.0AI短剧漫剧专用超真实感资产角色库Z-邻家AI大女孩_2043174607024295937.json, 图片生成/文生图/Z-image ZIT自定义风格+肖像大师一键生成定妆照工作流_2044646462713237506.json, 图片生成/文生图/Z-image ZIT自定义风格+肖像大师文生图_2042726424636821505.json, 图片生成/文生图/Z-image ZIT自定义风格+肖像大师超级手搓定妆照_2042427959553826817.json, 图片生成/文生图/Z-image ZIT自定义风格+肖像大师超级手搓定妆照_2042456216730869761.json, 图片生成/文生图/Z-image 自定义风格+肖像大师超级手搓定妆照_2044382790476636162.json, 图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2003676950780624897.json, 图片生成/文生图/Z-imageZIB+SeedVR2.5.1 超真实感定妆照文生图_1993888170003595266.json, 图片生成/文生图/巨牛Z-imageZIB+SeedVR2.5.1 超真实感定AI短剧定妆照文生图_2079579098531323905.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_checkpoint

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/反推提示词/85jiaosezichanku_2034622358798999554.json、图片生成/图生图/AI短剧文生空场景专用+自动扩写专用提示词-邻家AI大女孩_2043344708990144514.json、图片生成/图生图/AI短剧文生空场景专用Qwen-image+自动扩写专用提示词_1961070208133873665.json、图片生成/图生图/AI短剧文生空场景专用Qwen-image+自动扩写专用提示词_2039157804702900225.json、图片生成/文生图/AI短剧文生空场景专用Qwen-image+自动扩写专用提示词_2045052390331654146.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 17 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `WujiCleaner`
- `WujiEditor`
- `WujiUpscaler`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 14/17 个有
- `WujiSampler` —— 12/17 个有
- `WujiStyleSelector` —— 12/17 个有
- `PortraitMaster_中文版` —— 6/17 个有
- `ClownsharKSampler_Beta` —— 5/17 个有
- `ModelSamplingAuraFlow` —— 5/17 个有
- `VAEDecode` —— 5/17 个有
- `JWInteger` —— 4/17 个有
- `ClipLoaderGGUF` —— 2/17 个有
- `CompressImages` —— 1/17 个有
- `LoadImage` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | bong_tangent | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | -1 | -1 - -1 | 5 | 100% |
| 调度器 | 1 | 1 - 1 | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 bong_tangent，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，观测区间 -1 - -1，5 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
