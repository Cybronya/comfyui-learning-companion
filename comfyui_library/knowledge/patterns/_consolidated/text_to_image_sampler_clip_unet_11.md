---
name: text_to_image_sampler_clip_unet_11
type: Text To Image
frequency: 25
level: weak
coverage: 0.9528
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima基础工作流_2050251032118210561.json, 图片生成/文生图/boogu base文生图_2067452727042592770.json, 图片生成/文生图/boogu image turbo 文生图_2069087085788749825.json, 图片生成/文生图/boogu turbo批量文生图_2070386922110930945.json, 图片生成/文生图/boogu turbo文生图_2069610874171641858.json, 图片生成/文生图/boogu turbo文生图_2069633350947663873.json, 图片生成/文生图/boogu turbo文生图_2069634712343244801.json, 图片生成/文生图/boogu turbo文生图急速生图_2069629401351933954.json, 图片生成/文生图/boogu turbo文生图批量版_2070336788392144897.json, 图片生成/文生图/boogu turbo文生图批量版_2070422555663622146.json, 图片生成/文生图/boogu turbo文生图批量版_2070469626550644737.json, 图片生成/文生图/krea2文生图批量版_2070339623888441346.json, 图片生成/文生图/krea2文生图批量版_2070388445238878210.json, 图片生成/文生图/krea2文生图批量版_2070421570203508737.json, 图片生成/文生图/krea2文生图批量版_2070468131897827330.json, 图片生成/文生图/⚡ Boogu-Turbo 极速高写实文生图_2068717870527369217.json, 图片生成/文生图/【GUGU】Z-image文生图工作流_1993849344558383105.json, 图片生成/文生图/【阿良绘】boogu_turbo文生图工作流_2071226103880044545.json, 图片生成/文生图/太猛了！Z-image文生图新王-支持中文！_1995051018658492417.json, 图片生成/文生图/文生图-升级款 法老专用_2035629542928289793.json, 图片生成/文生图/文生图-升级款 法老专用_2046862125410295809.json, 图片生成/文生图/文生图千问qwen2512文生图阿里最新文生图开源模型_2006970243293388801.json, 图片生成/文生图/皮神-Zimage基础工作流_1996929661861040129.json, 图片生成/文生图/空白工作流_2051296618825175041.json, 图片生成/文生图/豹豹喵呜制作：百度模型和Z-image对比测试_2045066482610081794.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/anima基础工作流_2050251032118210561.json、图片生成/文生图/boogu base文生图_2067452727042592770.json、图片生成/文生图/boogu image turbo 文生图_2069087085788749825.json、图片生成/文生图/boogu turbo批量文生图_2070386922110930945.json、图片生成/文生图/boogu turbo文生图_2069610874171641858.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 23/25 个有
- `CR Text` —— 15/25 个有
- `HAIGC_SaveImagesToZip` —— 8/25 个有
- `PromptBatchQueue` —— 8/25 个有
- `FluxResolutionNode` —— 2/25 个有
- `ImageStitch` —— 1/25 个有
- `LoaderGGUF` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1600 | 25 | 83% |
| 高度 | 1536 | 544 - 1920 | 25 | 81% |
| 采样步数 | 8 | 4 - 50 | 25 | 4% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 4 | 25 | 28% |
| 采样算法 | euler | - | 25 | 64% |
| 调度器 | simple | - | 25 | 84% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1600，25 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 544 - 1920，25 个样本，取值集中（一致性 81%）
- 采样步数 中位数 8，观测区间 4 - 50，25 个样本，取值分散，一致性仅 4%
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 4，25 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，25 个样本，一致性 64%
- 调度器 最常用 simple，25 个样本，一致性 84%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（20/25 个样本）：Steps较低可能导致细节不足
