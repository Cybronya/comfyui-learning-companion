---
name: unknown_workflow_video_lora_sampler_92
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.76625
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/multitalk图片唱歌数字人对口型_1957667803581050882.json, 视频生成/图生视频/wanvideo_infinitetalk_单人工作流_1958061014984118274.json, 视频生成/图生视频/wanvideo_infinitetalk_双人工作流_1958075798320197633.json, 视频生成/图生视频/wanvideo_infinitetalk_图片转视频单人工作流_2014174614657703937.json, 视频生成/图生视频/❤最强数字人Infinitetalk+运镜参考版🌙_1977385230757699586.json, 视频生成/图生视频/图片转说话数字人 - Multitalk对口型优化版_1948766276714934274.json, 视频生成/图生视频/工作流视频篇12-AI图生数字人加运镜参考_2018299977335840769.json, 视频生成/图生视频/影视短剧导演之七：人物对口型_1989886464651612162.json, 视频生成/图生视频/电商-商用数字人 运镜版无限时长_可音频_视频切换_1986797048806764545.json, 视频生成/图生视频/电商带货商品展示数字人口播商用运镜版2.0【可切换】_1962734249734483970.json, 视频生成/图生视频/电商带货商品展示数字人口播商用运镜版2.0【可切换】_1971581572791136257.json, 视频生成/图生视频/音乐+数字人_1942210266623053825.json, 视频生成/图生视频/🥳infinitetalk最强数字人 运镜参考版【可切换】🐟_1958430229331132417.json, 视频生成/文生视频/Multitalk最强数字人运镜参考版 运行稳定版【8月6日日修复】_1936951987776704514.json, 视频生成/文生视频/最强数字人运镜_1947944588175650817.json, 视频生成/文生视频/💂‍Multitalk最强数字人 新手直出版 可出动物💂‍_1937688906760654850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_92

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/multitalk图片唱歌数字人对口型_1957667803581050882.json、视频生成/图生视频/wanvideo_infinitetalk_单人工作流_1958061014984118274.json、视频生成/图生视频/wanvideo_infinitetalk_双人工作流_1958075798320197633.json、视频生成/图生视频/wanvideo_infinitetalk_图片转视频单人工作流_2014174614657703937.json、视频生成/图生视频/❤最强数字人Infinitetalk+运镜参考版🌙_1977385230757699586.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 16 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 15/16 个有
- `LoadImage` —— 15/16 个有
- `AudioCrop` —— 14/16 个有
- `MultiTalkWav2VecEmbeds` —— 14/16 个有
- `VHS_LoadVideo` —— 14/16 个有
- `WanVideoTextEncode` —— 14/16 个有
- `INTConstant` —— 13/16 个有
- `JWIntegerToString` —— 13/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/16 个有
- `SimpleMath+` —— 13/16 个有
- `easy showAnything` —— 13/16 个有
- `CR Text` —— 12/16 个有
- `ImageResizeKJ` —— 12/16 个有
- `LayerUtility: PurgeVRAM V2` —— 12/16 个有
- `VHS_DuplicateImages` —— 12/16 个有
- `WanVideoImageToVideoEncode` —— 12/16 个有
- `WanVideoUni3C_ControlnetLoader` —— 12/16 个有
- `WanVideoUni3C_embeds` —— 12/16 个有
- `easy anythingIndexSwitch` —— 11/16 个有
- `WanVideoContextOptions` —— 10/16 个有
- `WanVideoTorchCompileSettings` —— 9/16 个有
- `WanVideoEncode` —— 8/16 个有
- `ImpactInt` —— 7/16 个有
- `easy int` —— 7/16 个有
- `ImageFromBatch+` —— 6/16 个有
- `PrimitiveInt` —— 6/16 个有
- `Int` —— 4/16 个有
- `RHHiddenNodes` —— 4/16 个有
- `WanVideoImageToVideoMultiTalk` —— 4/16 个有
- `GetNode` —— 3/16 个有
- `ImageResizeKJv2` —— 3/16 个有
- `SetNode` —— 3/16 个有
- `RH_Captioner` —— 2/16 个有
- `CR Text Concatenate` —— 1/16 个有
- `Note Plus (mtb)` —— 1/16 个有
- `PrimitiveBoolean` —— 1/16 个有
- `RH_Prompter` —— 1/16 个有
- `RH_Translator` —— 1/16 个有
- `ShowText|pysssss` —— 1/16 个有
- `Text Multiline` —— 1/16 个有
- `easy ifElse` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
