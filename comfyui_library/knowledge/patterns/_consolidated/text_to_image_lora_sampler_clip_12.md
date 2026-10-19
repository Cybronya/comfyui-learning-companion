---
name: text_to_image_lora_sampler_clip_12
type: Text To Image
frequency: 23
level: strong
coverage: 0.897826
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AI长视频导演台｜Minimax H3短剧漫剧人物一致分镜衔接_2092573469488795649.json, 视频生成/图生视频/H3 AI长视频导演台 短剧漫剧人物一致分镜丝滑衔接_2100673869026779138.json, 视频生成/图生视频/H3 Max Turbo图生视频 首尾帧视频生成工具_2099943877296877569.json, 视频生成/图生视频/H3 Max Turbo图生视频首尾帧生成全节点注释_2100286294709596162.json, 视频生成/图生视频/H3导演台开源版 图生视频多模态创作工具_2100283259153375234.json, 视频生成/图生视频/MiniMAX H3导演台｜图生视频一键出片_2092614529858490370.json, 视频生成/图生视频/MiniMax H3 Max Turbo极速版图生视频首尾帧处理工具_2102123247629332481.json, 视频生成/图生视频/MiniMax H3 Max Turbo极速版图生视频首尾帧，高速低成本流畅过渡方案_2103565859515101186.json, 视频生成/图生视频/MiniMax H3导演台开源版图生视频处理生成工具_2101753193574256642.json, 视频生成/图生视频/MiniMax H3导演台开源版视频处理生成工具_2101025178607243266.json, 视频生成/图生视频/MiniMax H3导演台开源版视频处理生成工具_2101041217042739201.json, 视频生成/图生视频/MiniMax H3导演台开源版视频处理生成工具_2101403892918603777.json, 视频生成/图生视频/MiniMax H3开源版基础工作流 图生视频视频生视频通用_2104325816313274370.json, 视频生成/图生视频/MiniMax H3长视频导演台，漫剧短剧人物一致分镜丝滑衔接图生视频_2103205976202633218.json, 视频生成/图生视频/Minimax H3 AI长视频导演台 短剧漫剧人物一致极速1080P_2108978521166143490.json, 视频生成/图生视频/Minimax H3 AI长视频导演台 短剧漫剧分镜丝滑衔接人物一致_2098642560595087361.json, 视频生成/图生视频/Minimax H3长视频导演台｜短剧漫剧分镜丝滑衔接_2098756338263355394.json, 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json, 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频生成_2093247372666167298.json, 视频生成/文生视频/H3 Max Turbo图生视频首尾帧生成 全节点注释_2099926302546550786.json, 视频生成/文生视频/MiniMax H3长视频导演台短剧漫剧人物一致分镜处理工具_2101400011450961921.json, 视频生成/文生视频/Minimax H3全能导演台｜短剧分镜丝滑衔接生成_2095094347023867905.json, 视频生成/文生视频/短剧分镜丝滑衔接｜Minimax H3全能导演台生成_2095053627458146306.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/AI长视频导演台｜Minimax H3短剧漫剧人物一致分镜衔接_2092573469488795649.json、视频生成/图生视频/H3 AI长视频导演台 短剧漫剧人物一致分镜丝滑衔接_2100673869026779138.json、视频生成/图生视频/H3 Max Turbo图生视频 首尾帧视频生成工具_2099943877296877569.json、视频生成/图生视频/H3 Max Turbo图生视频首尾帧生成全节点注释_2100286294709596162.json、视频生成/图生视频/H3导演台开源版 图生视频多模态创作工具_2100283259153375234.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 16/23 个有
- `MiniMaxH3TurboLoRA` —— 16/23 个有
- `ModelAttentionBackend` —— 16/23 个有
- `SaveImage` —— 16/23 个有
- `ComfyMiniMaxH3Director` —— 10/23 个有
- `MiniMaxH3EasyModelAdapter` —— 9/23 个有
- `LoadImage` —— 7/23 个有
- `MiniMaxH3Director` —— 6/23 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 5/23 个有
- `CR Text` —— 4/23 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 2/23 个有
- `EmptyImage` —— 1/23 个有
- `PreviewImage` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（24/23 个样本）：Steps较低可能导致细节不足
