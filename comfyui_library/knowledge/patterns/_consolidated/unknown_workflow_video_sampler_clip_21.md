---
name: unknown_workflow_video_sampler_clip_21
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.957737
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WANI2V彩色烟雾视频制作器-彩烟特效ZYP原创_1907459006556999682.json, 视频生成/图生视频/WAN复杂动作防崩图生视频工作流_1895519547200307202.json, 视频生成/图生视频/Wan2.1阿里通义万相图生视频工作流_1894957699035693057.json, 视频生成/图生视频/Wan图生视频高精度FP32版480P模型V1_1894619685634355201.json, 视频生成/图生视频/Wan图生视频高质量BF16版720P模型V1_1894653329455362049.json, 视频生成/图生视频/wan2.1通义万相图生视频蹦蹦跳跳工作流_1899811031231639553.json, 视频生成/图生视频/一键泄气特效-万相wan2.1新玩意_1899415692570181634.json, 视频生成/图生视频/万物被捏扁特效-万相wan2.1新玩意_1899312280767516673.json, 视频生成/图生视频/万相WAN2.1，美女一键跳舞！_1910726225436864514.json, 视频生成/图生视频/万相WAN2.1，美女一键跳舞！_1911140460969062401.json, 视频生成/图生视频/冲锋枪射击特效-万相wan2.1新玩意_1899671568367177729.json, 视频生成/图生视频/女子搏击，香香的粉拳-万相wan2.1_1900467836874301442.json, 视频生成/图生视频/摇摆舞蹈-Wan2.1_1955654165034930178.json, 视频生成/图生视频/新版360度旋转特效-万相wan_1899699069881860097.json, 视频生成/图生视频/新版360度旋转特效-万相wan_2005178859836370946.json, 视频生成/图生视频/火爆全网解压神器一起来切水果_1937513955088580610.json, 视频生成/图生视频/街霸特效超级波动拳-万相wan2.1_1899332733573746689.json, 视频生成/图生视频/被压扁特效-万相wan2.1新玩意_1899672945285877762.json, 视频生成/图生视频/解压神器，一起来切水晶--万相WAN2.1_1899288956402356225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/WANI2V彩色烟雾视频制作器-彩烟特效ZYP原创_1907459006556999682.json、视频生成/图生视频/WAN复杂动作防崩图生视频工作流_1895519547200307202.json、视频生成/图生视频/Wan2.1阿里通义万相图生视频工作流_1894957699035693057.json、视频生成/图生视频/Wan图生视频高精度FP32版480P模型V1_1894619685634355201.json、视频生成/图生视频/Wan图生视频高质量BF16版720P模型V1_1894653329455362049.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 19 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 15/19 个有
- `WanVideoEnhanceAVideo` —— 15/19 个有
- `WanVideoLoraSelect` —— 15/19 个有
- `Note Plus (mtb)` —— 13/19 个有
- `ImageUpscaleWithModel` —— 12/19 个有
- `UpscaleModelLoader` —— 12/19 个有
- `Int` —— 11/19 个有
- `WanVideoTeaCache` —— 11/19 个有
- `WanVideoTorchCompileSettings` —— 8/19 个有
- `GetImageSizeAndCount` —— 3/19 个有
- `Primitive integer [Crystools]` —— 2/19 个有
- `Primitive string [Crystools]` —— 2/19 个有
- `PrimitiveStringMultiline` —— 2/19 个有
- `LoadAudio` —— 1/19 个有
- `RHHiddenNodes` —— 1/19 个有
- `SaveLatent` —— 1/19 个有
- `SimpleMath+` —— 1/19 个有
- `WanVideoFreeInitArgs` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
