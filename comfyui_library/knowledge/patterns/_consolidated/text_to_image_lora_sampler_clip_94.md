---
name: text_to_image_lora_sampler_clip_94
type: Text To Image
frequency: 14
level: strong
coverage: 0.847286
common_nodes: [AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, EmptyYuE2LatentAudio, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, PreviewAny, SaveAudioAdvanced, SheetSage2AudioToABC, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YuE2GenerateMusic, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/YuE2音乐生成工作流_音频创作处理工具_2100746182380318721.json, 图片生成/文生图/YuE2音乐生成工作流_音频创作处理工具_2101457809861861378.json, 图片生成/文生图/YuE2音乐生成工作流_音频创作处理工具_2102592380288458754.json, 图片生成/文生图/YuE2音乐生成支持翻唱_音频创作处理工具_2100746485162930177.json, 图片生成/文生图/YuE2音乐生成支持翻唱_音频创作处理工具_2101458598911107074.json, 图片生成/文生图/YuE2音乐生成支持翻唱_音频创作处理工具_2102593981120081922.json, 图片生成/文生图/YuE2音乐生成翻唱音频创作处理工作流工具_2101786094982488065.json, 图片生成/文生图/yue2一键配乐超好听，数字人文生图音乐生成工作流_2112349434033033218.json, 图片生成/文生图/yue2音乐生成配乐工作流｜数字人歌曲一键直出｜超级好听MV配乐神器_2112124847831740418.json, 数字人/数字人/yue2音乐生成工作流，数字人配乐一键出超级好听_2110513129020026882.json, 数字人/数字人/yue2音乐生成工作流，数字人配乐一键出超级好听_2111644237338071041.json, 音频生成/音频生成/YuE2音乐生成ComfyUI音频创作处理工作流_2101030293187686401.json, 音频生成/音频生成/YuE2音乐生成工作流 音频创作处理工具_2099988070207676417.json, 音频生成/音频生成/YuE2音乐生成支持翻唱 音频创作处理工具_2099937977395924993.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/YuE2音乐生成工作流_音频创作处理工具_2100746182380318721.json、图片生成/文生图/YuE2音乐生成工作流_音频创作处理工具_2101457809861861378.json、图片生成/文生图/YuE2音乐生成工作流_音频创作处理工具_2102592380288458754.json、图片生成/文生图/YuE2音乐生成支持翻唱_音频创作处理工具_2100746485162930177.json、图片生成/文生图/YuE2音乐生成支持翻唱_音频创作处理工具_2101458598911107074.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `EmptyYuE2LatentAudio`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveAudioAdvanced`
- `SheetSage2AudioToABC`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `YuE2GenerateMusic`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 10/14 个有
- `EmptyImage` —— 10/14 个有
- `PreviewImage` —— 10/14 个有
- `VAEDecodeAudioTiled` —— 10/14 个有
- `YuE2GenerateABC` —— 10/14 个有
- `孤海注释` —— 9/14 个有
- `Fast Groups Muter (rgthree)` —— 5/14 个有
- `PrimitiveStringMultiline` —— 5/14 个有
- `Textbox` —— 5/14 个有
- `TrimAudioDuration` —— 5/14 个有
- `Apply Whisper` —— 4/14 个有
- `Audio Duration` —— 4/14 个有
- `AudioCrop` —— 4/14 个有
- `AudioSeparation` —— 4/14 个有
- `PreviewAudio` —— 4/14 个有
- `ShowText|pysssss` —— 4/14 个有
- `easy positive` —— 4/14 个有
- `SaveImage` —— 2/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（17/14 个样本）：Steps较低可能导致细节不足
