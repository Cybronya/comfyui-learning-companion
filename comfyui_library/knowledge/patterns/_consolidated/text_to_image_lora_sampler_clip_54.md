---
name: text_to_image_lora_sampler_clip_54
type: Text To Image
frequency: 19
level: strong
coverage: 0.939789
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Seedance2.5全参工作流｜图生图多模态参考｜可调参数全开放_2101900605341126657.json, 图片生成/图生图/Wan 2.7视频编辑换背景工作流｜一键替换场景背景｜视频处理必备_2099168088137752578.json, 数字人/数字人/一键数字人照片说话｜静态照片生成开口视频_2097224261978116098.json, 数字人/数字人/数字人口播形象视频｜口播带货数字人批量做_2097215283814559746.json, 视频生成/图生视频/SD2.5全能参考全参数版｜图生视频自由调控_2098757736740769793.json, 视频生成/图生视频/Seedance 2.5全参可调｜图生视频视频生视频一步到位_2099871193108140034.json, 视频生成/图生视频/Seedance 2.5全参工作流全参数输入视频生成，视频生视频图生视频方案_2105808093924909057.json, 视频生成/图生视频/Seedance 2.5全参工作流，视频生视频图生视频全覆盖方案_2106570538192822274.json, 视频生成/图生视频/Seedance 2.5动作迁移，人物场景特效图生视频_2111225027298414593.json, 视频生成/图生视频/Seedance2.5全参图生视频工作流｜视频生视频稳定出新_2108014164991102978.json, 视频生成/图生视频/Seedance2.5全参工作流 视频生成全模式处理工具_2113379825544159233.json, 视频生成/图生视频/Seedance2.5全参工作流｜视频生视频图生视频一网打尽_2100757319570247682.json, 视频生成/图生视频/Seedance2.5全参工作流｜视频生视频图生视频全能_2089422276826583041.json, 视频生成/图生视频/Seedance2.5全参工作流｜视频生视频图生视频全能生成_2097053723100008450.json, 视频生成/图生视频/Seedance2.5全参工作流｜视频生视频图生视频双通道高质输出_2114243356279787521.json, 视频生成/图生视频/Seedance2.5全参数视频工作流 图生视频与视频生视频_2098285496450510850.json, 视频生成/图生视频/Seedance_2.5多模态全能参考视频｜图生视频视频生视频双支持_2101899070481719297.json, 视频生成/图生视频/全参工作流｜Seedance2.5视频生视频图生视频_2090599945182212098.json, 视频生成/图生视频/全参视频工作流｜Seedance2.5图生视频生视频直出_2093483002692198401.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Seedance2.5全参工作流｜图生图多模态参考｜可调参数全开放_2101900605341126657.json、图片生成/图生图/Wan 2.7视频编辑换背景工作流｜一键替换场景背景｜视频处理必备_2099168088137752578.json、数字人/数字人/一键数字人照片说话｜静态照片生成开口视频_2097224261978116098.json、数字人/数字人/数字人口播形象视频｜口播带货数字人批量做_2097215283814559746.json、视频生成/图生视频/SD2.5全能参考全参数版｜图生视频自由调控_2098757736740769793.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 17/19 个有
- `LoadAudio` —— 16/19 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 16/19 个有
- `ttN text` —— 14/19 个有
- `SaveImage` —— 7/19 个有
- `EmptyImage` —— 2/19 个有
- `PreviewImage` —— 2/19 个有
- `PrimitiveStringMultiline` —— 2/19 个有
- `RH_KlingV2AiAvatarStandardImageAudioToVideo` —— 2/19 个有
- `MuyeTextEditOutput` —— 1/19 个有
- `RH_AlibabaWan27VideoEdit` —— 1/19 个有
- `RH_BytedanceDoubaoSeedAudio10` —— 1/19 个有
- `T8ShowText` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（20/19 个样本）：Steps较低可能导致细节不足
