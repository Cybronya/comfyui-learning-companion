# DeepTranslatorTextNode

## 节点类型

`DeepTranslatorTextNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输出

- `text:STRING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "english", "disable", "", "", "GoogleTranslator", "A colorful and modern advertisement poster, featuring Sailor`（3 次）
- `["auto", "english", false, "", "", "GoogleTranslator", "高分辨率，规则，完美", "proxy_hide", "authorization_hide"]`（2 次）
- `["auto", "english", false, "", "", "GoogleTranslator", "蛇缠绕美女", "proxy_hide", "authorization_hide"]`（1 次）
- `["auto", "english", false, "", "", "GoogleTranslator", "a high-resolution photograph featuring a young East Asian woman `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
