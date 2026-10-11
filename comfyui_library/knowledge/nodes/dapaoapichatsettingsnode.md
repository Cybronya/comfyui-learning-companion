# DapaoAPIChatSettingsNode

## 节点类型

`DapaoAPIChatSettingsNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `📝 系统提示词:STRING`（2 次）
- `🔢 最大历史轮数:INT`（2 次）
- `📤 最大生成token:INT`（2 次）
- `🌡️ 温度:FLOAT`（2 次）
- `🎯 top_p:FLOAT`（2 次）
- `🔝 top_k:INT`（2 次）
- `🔁 重复惩罚:FLOAT`（2 次）
- `📈 频率惩罚:FLOAT`（2 次）
- `📍 存在惩罚:FLOAT`（2 次）
- `🎲 随机种:INT`（2 次）

## 输出

- `⚙️对话设置:DAPAO_API_CHAT_SETTINGS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 100, 8192, 0.7, 0.9, 20, 1, 0, 0, 915631197227449, "randomize", false, 2048]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
