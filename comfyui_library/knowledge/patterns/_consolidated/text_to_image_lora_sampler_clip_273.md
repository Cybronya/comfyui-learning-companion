---
name: text_to_image_lora_sampler_clip_273
type: Text To Image
frequency: 7
level: strong
coverage: 0.906143
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/全噪影像预设工作流lite版 影像风格化处理_2109015110072229889.json, 图片生成/文生图/手机摄影随地大小拍v2｜真实感lora暗光噪点文生图对抗单反感_2088759074585407489.json, 图片生成/文生图/手机随手拍质感文生图 随地大小拍v3模拟生活化摄影_2104273094792802306.json, 图片生成/文生图/手机随拍感文生图｜随地大小拍写实图片生成工作流_2087230285426548737.json, 图片生成/文生图/手机随拍感真实质感lora｜随地大小拍对抗单反完美感文生图_2088762070585143297.json, 图片生成/文生图/随地大小拍手机摄影v2文生图写真创作工作流_2081761338916954114.json, 图片生成/文生图/随地大小拍手机摄影v3｜文生图出大片 手机随手拍质感拉满_2104084816416305153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_273

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/全噪影像预设工作流lite版 影像风格化处理_2109015110072229889.json、图片生成/文生图/手机摄影随地大小拍v2｜真实感lora暗光噪点文生图对抗单反感_2088759074585407489.json、图片生成/文生图/手机随手拍质感文生图 随地大小拍v3模拟生活化摄影_2104273094792802306.json、图片生成/文生图/手机随拍感文生图｜随地大小拍写实图片生成工作流_2087230285426548737.json、图片生成/文生图/手机随拍感真实质感lora｜随地大小拍对抗单反完美感文生图_2088762070585143297.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CLIPLoaderGGUF` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `LayerUtility: ImageTaggerSave` —— 1/7 个有
- `MoYouAddNoise` —— 1/7 个有
- `MoYouAutoLevelsAnalyze` —— 1/7 个有
- `MoYouAutoLevelsApply` —— 1/7 个有
- `MoyouShader` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
