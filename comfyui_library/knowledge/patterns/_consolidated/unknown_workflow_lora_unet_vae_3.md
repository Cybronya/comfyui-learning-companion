---
name: unknown_workflow_lora_unet_vae_3
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.911133
common_nodes: [CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫光斑光影增强_qwen 2511_2025486195010052098.json, 图片生成/图生图/千问Qwen-Edit-2511-产品单图融图_2062791307294240770.json, 图片生成/图生图/千问Qwen-Edit-2511-产品重打光溶图_2062795573585080321.json, 图片生成/图生图/千问Qwen-Edit-2511-人物&产品重打光_2062801026117365762.json, 图片生成/图生图/千问Qwen-Edit-2511-风格迁移_2062797855227727874.json, 图片生成/图生图/史上最强-小红书动漫转写实真人_2043235575892807682.json, 图片生成/图生图/史上最强-小红书动漫转写实真人（FireRed_OmniRealism）_2037918131322101761.json, 图片生成/图生图/史上最强-小红书动漫转写实真人（FireRed_OmniRealism）_2038424926553640962.json, 图片生成/图生图/小红书FireRed-Image-Edit1.1（单图、双图、三图编辑）_2029922206393831425.json, 图片生成/图生图/小红书_动漫转写实真人_2083827042285604866.json, 图片生成/图生图/小红书模型动漫转真人_2067301137937686530.json, 图片生成/图生图/涂鸦控制_海报设计_2026556702794977281.json, 图片生成/图生图/涂鸦控制_海报设计_2026672287650418690.json, 平台全量/Qwen Eedit 2511 升级版 角色扮演 Cosplay 任何角色 万物风格迁移卡通动漫装扮_2029037972955340802.json, 平台全量/qwen2511零偏移图像编辑_2004898730488856578.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/动漫光斑光影增强_qwen 2511_2025486195010052098.json、图片生成/图生图/千问Qwen-Edit-2511-产品单图融图_2062791307294240770.json、图片生成/图生图/千问Qwen-Edit-2511-产品重打光溶图_2062795573585080321.json、图片生成/图生图/千问Qwen-Edit-2511-人物&产品重打光_2062801026117365762.json、图片生成/图生图/千问Qwen-Edit-2511-风格迁移_2062797855227727874.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 11/15 个有
- `VAEDecode` —— 11/15 个有
- `Easy_QwenEdit2509` —— 10/15 个有
- `Image Comparer (rgthree)` —— 10/15 个有
- `Seed (rgthree)` —— 6/15 个有
- `QwenImageIntegratedKSampler` —— 4/15 个有
- `CR Text` —— 2/15 个有
- `ConditioningZeroOut` —— 1/15 个有
- `ImageStitch` —— 1/15 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | res_2m | - | 15 | 40% |
| 调度器 | sgm_uniform | - | 15 | 40% |
| 重绘幅度 | 1 | 1 - 999 | 15 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，15 个样本，一致性 40%
- 调度器 最常用 sgm_uniform，15 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 999，15 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 999，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（11/15 个样本）：Steps较低可能导致细节不足
