---
name: text_to_image_lora_sampler_clip_226
type: Text To Image
frequency: 9
level: strong
coverage: 0.897444
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax导演台全能工作流-图生视频工作流_2087382195718676481.json, 视频生成/图生视频/Minimax H3长视频导演台｜短剧漫剧分镜丝滑衔接_2098756338263355394.json, 视频生成/图生视频/RIFE丝滑慢动作｜视频慢放不丢帧不掉质感_2097229853106987009.json, 视频生成/图生视频/RIFE视频补帧到60帧｜卡顿画面秒变丝滑_2097228457901117441.json, 视频生成/图生视频/宗门神曲多人替换演示导演台加速版全能工作流MiniMax_2087431272393166850.json, 视频生成/图生视频/视频补帧到60帧工作流｜RIFE插帧画面流畅增强处理_2097165055967191041.json, 视频生成/文生视频/MiniMax H3长视频导演台短剧漫剧人物一致分镜处理工具_2101400011450961921.json, 视频生成/文生视频/Minimax H3全能导演台｜短剧分镜丝滑衔接生成_2095094347023867905.json, 视频生成/文生视频/短剧分镜丝滑衔接｜Minimax H3全能导演台生成_2095053627458146306.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_226

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax导演台全能工作流-图生视频工作流_2087382195718676481.json、视频生成/图生视频/Minimax H3长视频导演台｜短剧漫剧分镜丝滑衔接_2098756338263355394.json、视频生成/图生视频/RIFE丝滑慢动作｜视频慢放不丢帧不掉质感_2097229853106987009.json、视频生成/图生视频/RIFE视频补帧到60帧｜卡顿画面秒变丝滑_2097228457901117441.json、视频生成/图生视频/宗门神曲多人替换演示导演台加速版全能工作流MiniMax_2087431272393166850.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
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
- `ComfyMiniMaxH3Director` —— 4/9 个有
- `MiniMaxH3EasyModelAdapter` —— 4/9 个有
- `MiniMaxH3TurboLoRA` —— 4/9 个有
- `ModelAttentionBackend` —— 4/9 个有
- `FL_RIFE` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `MiniMaxH3Director` —— 2/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
